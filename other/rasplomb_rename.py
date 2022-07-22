import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

path = DATA_PATH + 'rasplomb/'
a = os.listdir(DATA_PATH + 'rasplomb/')
for aa in a:
    sn = aa.split('.')
    serial_full = sn[0]
    suffiks = sn[1]
    serial_short = serial_full[2:]
    term = get_listvec = get_list(f"SELECT termial FROM terminals WHERE serial_number LIKE '%{serial_short}'")[0]
    new_name = path + f'{term}_rasplomb_{serial_full}.{suffiks}'
    old_name = path + aa
    os.rename(old_name, new_name)
    print(new_name)

