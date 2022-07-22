import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, insert_all_otbor


class OtborSerialFile():
    def __init__(self):
        self.serials = file_to_arr(IN_DATA_PATH + 'otbor_serial.csv')
        
    def main_otbor_serial_file(self):     
        info = ''
        arr = []
        for term, dep in get_data(f"SELECT termial, department FROM terminals WHERE department = '{choise}'"):
            term = get_term_by_serial(serial)
            if not term:
                continue
            #print(term)
            dep = term[:7]
            #info += f'{term} {dep}\n'
            try:
                arr.append([term, dep])
            except Exception as ex:
                info += f'>> {ex} {serial} {term}\n'
                #print(f'>> {ex} {serial} {term}\n')
        insert_all_otbor(arr)
        self.info = info + f'{len(arr)}'


#u = OtborSerialFile()
#u.main_otbor_serial_file()