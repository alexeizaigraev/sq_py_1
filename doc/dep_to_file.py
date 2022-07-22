import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa_table import *


class DepToFile():

    def main_dep_to_file(self):

        query = 'SELECT * from departments ORDER BY department' 

        head = "department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner name;id_terminal;koatu;tax_id;koatu2"
        fName = "departments.csv"
        self.info = doc_papa_table(query, head, fName)
        