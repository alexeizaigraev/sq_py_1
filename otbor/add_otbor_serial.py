import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


class OtborSerial():
    def __init__(self, choise):
        if ' ' in choise:
            self.serials = choise.split(' ')
        else:
            self.serials = [choise,]
        
    def main_otbor_serial(self):     
        info = ''
        arr = []
        for serial in self.serials:
            term = get_term_by_serial(serial)
            dep = term[:7]
            info += f'{term} {dep}\n'
            arr.append([term, dep])
        insert_all_otbor(arr)
        self.info = info


#u = OtborSerial('КС00002390')
#u.main_otbor_serial()