import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from papa_pg import *

def main():
    info = ''
    

    #clear_table('otbor')
    clear_table('terminals')
    clear_table('departments')
    

    info += refresh_deps_from_gdrive() + '\n'
    info += refresh_terms_from_gdrive() + '\n'
    return info
