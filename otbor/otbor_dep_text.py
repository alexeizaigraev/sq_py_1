import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, insert_all_otbor


def main(choises):
    if ' ' in choises:
        choises = choises.split(' ')
    elif '\n' in choises:
        choises = choises.split('\n')
    else:
        choises = [choises,]

    info = ''
    arr = []
    for choise in choises:
        if not choise:
            continue
        vec = get_data(f"SELECT termial, department FROM terminals WHERE department = '{choise}'")
        arr += [(t, d) for t, d in vec if t]
    insert_all_otbor(arr)
    return f'{len(arr)}'


print(main('1010110 1010120'))
#main('80\n90')