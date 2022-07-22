import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, insert_all_otbor

def main():
    fiscals = file_to_arr(IN_DATA_PATH + 'otbor_fiscal.csv')
    info = ''
    arr = []
    for fiscal in fiscals:
        term, dep = get_data(f"SELECT termial, department FROM terminals WHERE fiscal_number = '{fiscal}'")[0]
        if not term:
            continue
        try:
            arr.append([term, dep])
        except Exception as ex:
            info += f'>> {ex} {fiscal} {term}\n'
    insert_all_otbor(arr)
    return f'{len(arr)}'


#u = OtborFiscalFile()
#u.main_otbor_fiscal_file()