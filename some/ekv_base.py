# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
from papa_pg import *

def mk_data():
    q = """
    SELECT departments.partner,
	terminals.termial, terminals.department,
	terminals.serial_number, terminals.fiscal_number,
	ekv.status,
	departments.region, departments.city, departments.address,
    departments.edrpou
FROM public.terminals, public.ekv, public.departments
WHERE terminals.fiscal_number = ekv.fiscal
AND departments.department = terminals.department
ORDER BY terminals.termial
"""
    return get_data(q)


def sum_activ_dep(partner):
    sum = 0
    for line in data:
        if partner == line[0] and sign_active in line[5] and line[-1]:
            sum += 1
    return sum

def sum_activ_pnfp(partner):
    sum = 0
    for line in data:
        if partner == line[0] and sign_active in line[5] and not line[-1]:
            sum += 1
    return sum

def sum_dep(partner):
    sum = 0
    for line in data:
        if partner == line[0] and line[-1]:
            sum += 1
    return sum

def sum_pnfp(partner):
    sum = 0
    for line in data:
        if partner == line[0] and not line[-1]:
            sum += 1
    return sum




def main():
    #ekv_from_file_full()
    
    dep = 0
    pnfp = 0

    activ_dep = 0
    activ_pnfp = 0

    all = 0
    out_text = ';;Відділення; та ПНФП;Робочі\n'
    out_text += f';{now_date_normal()};Відділення;ПНФП;Відділення;ПНФП\n'
    coco = 0
    partners = get_partners()
    for partner in partners:
        dep_partner = sum_dep(partner)
        dep += dep_partner

        pnfp_partner = sum_pnfp(partner)
        pnfp += pnfp_partner

        activ_dep_partner = sum_activ_dep(partner)
        activ_dep += activ_dep_partner

        activ_pnfp_partner = sum_activ_pnfp(partner)
        activ_pnfp += activ_pnfp_partner

        if dep_partner == 0 and pnfp_partner == 0:
            continue
        coco += 1
        out_line = f'{coco};{partner};{dep_partner};{pnfp_partner};{activ_dep_partner};{activ_pnfp_partner}'
        out_text += out_line + '\n'
        
    #out_text += '________________\nвсего;отделения;ПНФП;aктивные отделения;aктивные ПНФП\n'
    out_text += f';Всього;{dep};{pnfp};{activ_dep};{activ_pnfp}\n'
    inf = out_text
    out_text += '\n________________\n'
    out_text += 'партнёр;терминал;отделение;ЗН;ФН;статус;область;город;адрес;едрпоу\n'
    
    for line in data:
        out_text += ';'.join(line) + '\n'
    out_fname = OUT_DATA_PATH + 'DOC/' + 'Ekv.csv'
    text_to_file(out_text, out_fname)
    #save_and_show(out_text, out_fname)

    return inf + '\n\n' + out_fname



data = mk_data()
sign_active = 'Активний'
sign_noactive = 'Заблокований'

#main()