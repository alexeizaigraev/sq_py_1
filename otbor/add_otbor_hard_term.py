import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


class OtborHardTerm():
    def __init__(self, choise):
        if ' ' in choise:
            self.terms = choise.split(' ')
        else:
            self.terms = [choise,]
        
    def main_otbor_hard_term(self):
        info = ''
        arr = []
        terms = self.terms
        for term in terms:
            if len(term) < len( terms[0]):
                term = terms[0] [: (len(terms[0]) - len(term))] + term
            dep = term[:7]
            info += f'{term} {dep}\n'
            arr.append([term, dep])
        insert_all_otbor(arr)
        self.info = info

