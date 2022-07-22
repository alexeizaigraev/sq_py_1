import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, insert_all_otbor


def main(choise):
    if ' ' in choise:
        fiscals = choise.split(' ')
    elif '\n' in choise:
        fiscals = choise.split('\n')
    else:
        fiscals = [choise,]

    info = ''
    arr = []
    for fiscal in fiscals:
        if not fiscal:
            continue
        vec = get_data(f"SELECT termial, department FROM terminals WHERE fiscal_number LIKE '%{fiscal}'")
        arr += [(t, d) for t, d in vec if t]
    insert_all_otbor(arr)
    return f'{len(arr)}'


#print(main('80 90'))
#main('80\n90')