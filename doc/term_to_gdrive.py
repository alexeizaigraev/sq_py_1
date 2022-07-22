import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa_table import *


class TermToGdrive():

    def main_term_to_gdrive(self):
        query = "SELECT * FROM public.terminals ORDER BY termial;"
        
        head = "department;termial;model;serial_number;date_manufacture;soft;producer;rne_rro;sealing;fiscal_number;oro_serial;oro_number;ticket_serial;ticket_1sheet;ticket_number;sending;books_arhiv;tickets_arhiv;to_rro;owner_rro;register;finish"
        
        fName = "terminals.csv"
        self.info = doc_papa_table(query, head, fName)
        docPath = GDRIVE_BACKUP_PATH
        fout = docPath + fName
        txt = file_to_text_nosharp(fout)
        text_to_file(txt.replace(' 0:00:00', '').replace('null', ''), fout)
        