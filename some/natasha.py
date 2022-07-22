# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 


from modules import *
#from papa import *
from papa_pg import *
from datetime import datetime, date

def get_natasha_data():
    query = f'''SELECT department, edrpou, partner FROM departments
ORDER BY partner'''
    return get_data(query)

def count_comon(partner):
    count = 0
    for line in access_data:
        if partner in line[-1] and line[0] in natasha:
            count += 1
    return count

def count_edrpou(partner):
    count = 0
    for line in access_data:
        if partner in line[-1] and line[0] in natasha and line[1]:
            count += 1
    return(count)

def count_pnfp(partner):
    count = 0
    for line in access_data:
        if partner in line[-1] and line[0] in natasha and not line[1]:
            count += 1
    return count


def main():
    partner_dict = dict()
    for line in access_data:
        partner_dict[ line[-1] ] = line[0][:4]

    partner_list = sorted( partner_dict.keys() )
    header = 'Партнёр;Отделения с ЕДРПОУ;ПНФП;Всего'
    out_text = header + '\n'
    #print('\n\n' + header)
    summ_comon = 0
    summ_edrpou = 0
    summ_pnfp = 0
    for partner in partner_list:
        if partner and partner != 'intime' and count_comon(partner) > 0:
            out_line = f'{partner};{count_edrpou(partner)};{count_pnfp(partner)};{count_comon(partner)}'
            #print(out_line)
            out_text += out_line + '\n'
            summ_comon += count_comon(partner)
            summ_edrpou += count_edrpou(partner)
            summ_pnfp += count_pnfp(partner)

    out_text += '\n'
    #print(out_text)

    #print('Всего с ЕДРПОУ', summ_edrpou)
    out_text += f'Всего с ЕДРПОУ {summ_edrpou}\n'
    #print('Всего ПНФП', summ_pnfp)
    out_text += f'Всего ПНФП {summ_pnfp}\n'
    #print('Всего', summ_comon)
    out_text += f'Всего {summ_comon}\n'

    info = '\n\n' + out_text

    now = str(datetime.today())[:10]
    ofname = DATA_PATH + f'STATISTICA/{now}.csv'
    info += f'\n\n{ofname}'
    save_and_show(out_text, ofname)
    return info

natasha = set(mk_natasha())
access_data = get_natasha_data()
                
