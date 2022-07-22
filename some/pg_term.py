import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *
import os


class Term():

    def get_terms_data(self):
        query = '''SELECT otbor.term, departments.id_terminal, departments.city,departments.region, 
    departments.street_type, departments.street, departments.hous, 
    terminals.serial_number, terminals.fiscal_number
    FROM otbor, terminals, departments
    WHERE otbor.term = terminals.termial
    AND departments.department = terminals.department
    ORDER BY terminals.termial;'''
        return get_data(query)

    

    def main_term(self):
        info = ''
        data = self.get_terms_data()
        line = ''
        self.ag_cog = ''

        self.ColDataShablon1 = 5
        self.ColDataShablon2 = 6
        self.ColDataSoft = 7
        self.ColDataLimit = 8

        self.ColTermTerm = 0
        self.ColTermId = 1
        self.ColTermSity = 2
        self.ColTermRegion = 3
        self.ColTermStreet = 4
        self.ColTermHouse = 5
        self.ColTermSerial = 6


        fname_out = 'OutTerminals.csv'
        out_text = ''

        for line in data:
            terminal = line[0]
            idd = line[1]
            if not idd:
                idd = terminal
                
            sity = line[2]
            region = line[3]
            if not region:
                region = sity

            street_type = line[4]
            street = line[5]
            house = line[6]

            serial = line[7]
            if serial and '0' or 'O' in serial:
                serial = ''.join(line[7].split('0')[1:])
            if not serial:
                serial = line[8]
            if not serial:
                serial = '333'

            self.ag_cod = terminal[:3]

            out_line = ( terminal + ';'
                +idd + ';' +
                get_list(f"""SELECT term_owner FROM comon_data WHERE code = '{self.ag_cod}';""")[0]  + ';' +
                sity + ', ' + region + ';' +
                street_type + ' ' + street + ', ' + house + ';' +
                get_list(f"""SELECT term_shablon FROM comon_data WHERE code = '{self.ag_cod}';""")[0]  + ';' +
                get_list(f"""SELECT soft_version FROM comon_data WHERE code = '{self.ag_cod}';""")[0]  + ';' +
                get_list(f"""SELECT limit_kass FROM comon_data WHERE code = '{self.ag_cod}';""")[0]  + ';' +
                serial
            )
            

            out_text += out_line + "\n"
            #print(f'{Fore.BLUE} {out_line}')
            #p_green(out_line)
        full_out_fname = OUT_DATA_PATH + fname_out
        info += out_text + '\n\n'
        info += text_to_file(out_text, full_out_fname)
        self.info = info

#u = Term()
#u.main_term()