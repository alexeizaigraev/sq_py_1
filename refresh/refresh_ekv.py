import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from papa_pg import ekv_from_indata_full, clear_table, tickets_arhiv_update

def main():
    info = ''
    clear_table('ekv')
    info += ekv_from_indata_full()
    info += tickets_arhiv_update()
    return info
