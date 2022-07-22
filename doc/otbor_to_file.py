import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa_table import *


class OtborToFile():

    def main_otbor_to_file(self):

        query = 'SELECT * from otbor ORDER BY term' 

        head = "term;dep;"
        fName = "departments.csv"
        self.info = doc_papa_table(query, head, fName)
        