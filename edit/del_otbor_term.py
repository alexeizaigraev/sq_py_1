import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class DelOtborTerm():

    def main_del_otbor_term(self):
        info = ''
        q = 'SELECT * FROM OTBOR'
        otbor = get_data(q)
        for line in otbor:
            term = line[0]
            del_term(term)
            info += f'- {term}\n'
        self.info = info


