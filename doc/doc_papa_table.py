import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *

from papa_pg import get_data

def doc_papa_table(query, head, ofName):
    docPath = OUT_DATA_PATH + 'DOC/'
    info = ''
    if head:
        info = head + '\n'
    data = get_data(query)
    for line in data:
        info += f'{";".join(line)}\n'

    fout = docPath + ofName
    text_to_file(info, fout)
    #save_and_show(info, fout)
    return fout
 