# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
from papa_pg import *

def arr_to_dict(a):
    h = dict()
    for line in a:
        h[line[0]] = line[1]
    return h

def sum_noown_rro():
    h = dict()
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND terminals.owner_rro != 'eps'
	AND terminals.owner_rro != 'mist'
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))


def sum_own_rro():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND (
		terminals.owner_rro = 'eps'
	OR terminals.owner_rro = 'mist'
	)
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))

def sum_all_rro():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))


def sum_activ_rro():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND ekv.status = 'Активний'
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))

def sum_noactiv_rro():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND ekv.status != 'Активний'
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))


def sum_activ_dep():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND ekv.status != 'Активний'
	AND departments.edrpou != ''
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))

def sum_activ_pnfp():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND ekv.status != 'Активний'
	AND departments.edrpou = ''
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))

def sum_dep():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND departments.edrpou != ''
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))

def sum_pnfp():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM public.terminals, public.departments, public.ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND departments.edrpou = ''
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))

def get_line(h, partner):
    try:
        if partner in h:
            return str(h[partner])
        else:
            return '0'
    except:
        return '0'


def main():
    inf = ''
    partners = get_partners()
    q_dep = sum_dep()
    q_pnfp = sum_pnfp()
    q_activ_dep = sum_activ_dep()
    q_activ_pnfp = sum_activ_pnfp()
    q_activ_rro = sum_activ_rro()
    q_noactiv_rro = sum_noactiv_rro()
    q_own = sum_own_rro()
    q_noown = sum_noown_rro()
    q_allrro = sum_all_rro()

    out_text = 'partner;dep;pnfp;aktiv_dep;aktiv_pnfp;aktiv_rro;noaktiv_rro;own;noown;all_rro;return\n'
    for partner in partners:
        line = f'{partner};'
        
        line += get_line(q_dep, partner) + ';'
        line += get_line(q_pnfp, partner) + ';'
        
        line += get_line(q_activ_dep, partner) + ';'
        line += get_line(q_activ_pnfp, partner) + ';'

        line += get_line(q_activ_rro, partner) + ';'
        line += get_line(q_noactiv_rro, partner) + ';'

        line += get_line(q_own, partner) + ';'
        line += get_line(q_noown, partner) + ';'
        line += get_line(q_allrro, partner) + ';'
        
        out_text += line + '\n'

    out_fname = OUT_DATA_PATH + 'DOC/' + 'Ekv.csv'
    text_to_file(out_text, out_fname)
    #save_and_show(out_text, out_fname)

    return inf + out_text + '\n\n' + out_fname



sign_active = 'Активний'
sign_noactive = 'Заблокований'
sign_priostanov = 'Призупинений'

print(main())
