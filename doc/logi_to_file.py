import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa import *


class LogiToFile():

    def main_logi_to_file(self):
        query = "SELECT department, termial, serial_number, address, datalog, kind FROM logi ORDER BY datalog;"
        
        head = "num;department;termial;serial_number;address;datalog;kind"
        
        fName = "logi.csv"
        self.info = doc_papa(query, head, fName)
        