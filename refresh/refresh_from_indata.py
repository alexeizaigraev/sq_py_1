import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import subprocess
#from modules import file_to_vec
from papa_pg import *

def main():
    info = ''
    """
    app_path = 'C:/SharpForPy/SharpForPy.exe'
    try:
        subprocess.run(app_path)
        info += '\n\tsuccess sharp\n\n'
    except Exception as ex:
        info += '\n>> no start sharp\n\n'
"""
    #clear_table('otbor')
    clear_table('terminals')
    clear_table('departments')
    
    #info += refresh_otbor_from_indata() + '\n'
    info += refresh_deps_from_indata() + '\n'
    info += refresh_terms_from_indata() + '\n'
    
    
    #info += 'term ok\n'
    return info

print(main())
