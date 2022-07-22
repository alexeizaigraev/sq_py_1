import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class OtborHard():
    def __init__(self, terms_choise):
        self.terms = terms_choise
        
    def main_otbor_hard(self):     
        info = ''
        arr = []
        for term in self.terms:
            dep = term[:7]
            info += f'{term} {dep}\n'
            arr.append([term, dep])
        insert_all_otbor(arr)
        self.info = info

