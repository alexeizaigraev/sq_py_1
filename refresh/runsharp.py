import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import subprocess
#from modules import file_to_vec
import papa_pg as papa_pg

def main():
    info = ''
 
    #app_path = file_to_vec('Config/app_path.txt')[0]
    app_path = 'C:/SharpForPy/SharpForPy.exe'
    try:
        #os.startfile('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
        subprocess.run(app_path)
        info += '\n\tsuccess sharp\n\n'
    except Exception as ex:
        info += '\n>> no start sharp\n\n'


    papa_pg.clear_table('otbor')
    papa_pg.clear_table('terminals')
    papa_pg.clear_table('departments')
    

    info += papa_pg.otbor_from_file_full()
    info += papa_pg.dep_from_file_full() + '\n'
    info += papa_pg.term_from_file_full() + '\n'
    return info
