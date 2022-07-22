import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc.doc_papa_activ import *
#from papa_pg import get_ekv_fiscal_activ

class DeActivaciya():

    def main_deactivaciya(self):
        #ekv_fiscal_activ = get_ekv_fiscal_activ()

        query = """SELECT terminals.department, departments.address,
        terminals.serial_number, terminals.fiscal_number
        FROM terminals, departments, otbor
        WHERE terminals.termial = otbor.term
        AND departments.department = otbor.dep;"""

        head = "№ п/п;№ відділення ТОВ«ЕПС»;Адреса відділення; ЗН;ФН;Дата"
        fName = "Activaciya.csv"
        self.info = doc_papa_activ(query, head, fName, False)

#u = DeActivaciya()
#print(u.main_deactivaciya())