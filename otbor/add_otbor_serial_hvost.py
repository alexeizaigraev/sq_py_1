import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


class OtborSerialHvost():
    def __init__(self, choise):
        self.choise = choise
        
    def main_otbor_serial_hvost(self):
        info = ''
        arr = []
        for term in get_term_by_serial_hvost(self.choise):
            dep = term[:7]
            info += f'{term} {dep}\n'
            arr.append([term, dep])
        insert_all_otbor(arr)
        self.info = info


#u = OtborSerialHvost('2390, 888')
#u.main_otbor_serial_hvost()
#print(u.info)