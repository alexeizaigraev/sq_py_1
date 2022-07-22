import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, insert_all_otbor


def main(choise):
    if ' ' in choise:
        terminals = choise.split(' ')
    elif '\n' in choise:
        terminals = choise.split('\n')
    else:
        terminals = [choise,]
    arr = []
    for term in terminals:
        if not term:
            continue
        dep = term[:7]
        arr.append([term, dep])
        print(arr)
    insert_all_otbor(arr)
    return f'{len(arr)}'


#print(main('10101101\n10101201'))
#main('80\n90')