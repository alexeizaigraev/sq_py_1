import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, insert_all_otbor


def main(choise):
    if ' ' in choise:
        deps = choise.split(' ')
    elif '\n' in choise:
        deps = choise.split('\n')
    else:
        deps = [choise,]
    arr = []
    for dep in deps:
        if not dep:
            continue
        vec = get_data(f"SELECT termial, department FROM terminals WHERE department = '{dep}'")
        arr += [(t, d) for t, d in vec if t]
    insert_all_otbor(arr)
    return f'{len(arr)}'


#print(main('10101101 10101201'))
#main('80\n90')