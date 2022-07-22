import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from datetime import datetime
from modules import *

from papa_pg import get_data


class DocPgBack():

    def doc_pg_backup(self, query, head, ofName):
        #now = now_date_log()
        ddd = datetime.now().date()
        d = str(ddd.day)
        if len(d) == 1:
            d = '0' + d
        m = str(ddd.month)
        if len(m) == 1:
            m = '0' + m
        y = str(ddd.year)
        nau = f'{y}.{m}.{d}'
        out_path = f'{GDRIVE_PATH}PG_BACKUP/{nau}_{ofName}'
        info = ''
        if head:
            info = head + '\n'
        data = get_data(query)
        for line in data:
            info += f'{";".join(line)}\n'

        info = info.replace(" 0:00:00", "").replace("null", "")
        print()
        self.info += text_to_file(info, out_path) + '\n'
        
    def main_doc_pg_back(self):
        self.info = ''
        query = 'SELECT * FROM public.departments;'
        head = 'department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner name;id_terminal;koatu;tax_id;koatu2'
        fName = "departments.csv"
        self.doc_pg_backup(query, head, fName)

        query = 'SELECT * FROM public.terminals;'
        head = 'department;termial;model;serial_number;date_manufacture;soft;producer;rne_rro;sealing;fiscal_number;oro_serial;oro_number;ticket_serial;ticket_1sheet;ticket_number;sending;books_arhiv;tickets_arhiv;to_rro;owner_rro;register;finish'
        fName = "terminals.csv"
        self.doc_pg_backup(query, head, fName)
