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
    arr = []
    for choise in choises:
        vec = get_data(f"SELECT termial, department FROM terminals WHERE serial_number LIKE '%{choise}'")
        arr += [(t, d) for t, d in vec if t]
    insert_all_otbor(arr)
    return f'{len(arr)}'


#print(main('80 29 90'))