import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *

from papa_pg import get_data, get_ekv_fiscal_activ, refresh_one_ekv

def doc_papa_activ(query, head, ofName, flag_activ):
    ekv_fiscal_activ = get_ekv_fiscal_activ()
    docPath = OUT_DATA_PATH + 'DOC/'
    info = ''
    if head:
        info = head + '\n'
    data = get_data(query)
    count = 0
    for line in data:
        fiscal = line[3]
        if flag_activ:
            if fiscal in ekv_fiscal_activ:
                continue
        else:
            if fiscal not in ekv_fiscal_activ:
                continue
        #print(fiscal)
        count += 1
        info += f'{count};{";".join(line)};{now_date_normal()}\n'
        if flag_activ:
            refresh_one_ekv([fiscal, 'Активний'])
        else:
            refresh_one_ekv([fiscal, 'Заблокований'])
    fout = docPath + ofName
    text_to_file(info, fout)
    #save_and_show(info, fout)
    return fout + f'\n\n{info}'
 