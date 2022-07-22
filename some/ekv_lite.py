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
	FROM terminals, departments, ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
	AND terminals.owner_rro != 'eps'
	AND terminals.owner_rro != 'mist'
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))


def sum_own_rro():
    q = f"""SELECT DISTINCT departments.partner, COUNT(*)
	FROM terminals, departments, ekv
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
	FROM terminals, departments, ekv
	WHERE terminals.department = departments.department
	AND terminals.fiscal_number = ekv.fiscal
GROUP BY departments.partner;"""    
    return arr_to_dict(get_data(q))


def sum_activ_rro():
    q = f"""SELECT ddd.partner, COUNT(ttt.termial)
	FROM terminals ttt
	INNER JOIN departments ddd
	ON ttt.department = ddd.department
	AND ttt.tickets_arhiv = 'Активний'
GROUP BY ddd.partner
ORDER BY ddd.partner;"""    
    return arr_to_dict(get_data(q))

def sum_noactiv_rro():
    q = f"""SELECT ddd.partner, COUNT(ttt.termial)
	FROM terminals ttt
	INNER JOIN departments ddd
	ON ttt.department = ddd.department
	AND (
		ttt.tickets_arhiv = 'Заблокований'
		OR ttt.tickets_arhiv = 'Призупинений'
		)
GROUP BY ddd.partner
ORDER BY ddd.partner;"""    
    return arr_to_dict(get_data(q))


def sum_activ_dep():
    q = f"""SELECT ddd.partner, COUNT(ttt.termial)
	FROM terminals ttt
	INNER JOIN departments ddd
	ON ttt.department = ddd.department
	AND ttt.tickets_arhiv = 'Активний'
	AND ddd.edrpou != ''
GROUP BY ddd.partner
ORDER BY ddd.partner;"""    
    return arr_to_dict(get_data(q))

def sum_activ_pnfp():
    q = f"""SELECT ddd.partner, COUNT(ttt.termial)
	FROM terminals ttt
	INNER JOIN departments ddd
	ON ttt.department = ddd.department
	AND ttt.tickets_arhiv = 'Активний'
	AND ddd.edrpou = ''
GROUP BY ddd.partner
ORDER BY ddd.partner;"""    
    return arr_to_dict(get_data(q))

def sum_dep():
    q = f"""SELECT DISTINCT ddd.partner, COUNT(*)
	FROM departments ddd
	WHERE ddd.edrpou != ''
GROUP BY ddd.partner;"""    
    return arr_to_dict(get_data(q))

def sum_pnfp():
    q = f"""SELECT DISTINCT ddd.partner, COUNT(*)
	FROM departments ddd
	WHERE ddd.edrpou = ''
GROUP BY ddd.partner;"""    
    return arr_to_dict(get_data(q))

def get_line(h, partner):
    try:
        if partner in h:
            return str(h[partner])
        else:
            return '0'
    except:
        return '0'


def mk_data():
    q = """
    SELECT departments.partner,
	terminals.termial, terminals.department,
	terminals.serial_number, terminals.fiscal_number,
	ekv.status,
	departments.region, departments.city, departments.address,
    departments.edrpou
FROM terminals, ekv, departments
WHERE terminals.fiscal_number = ekv.fiscal
AND departments.department = terminals.department
ORDER BY terminals.termial
"""
    return get_data(q)

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

    c_dep = 0
    c_pnfp = 0
    c_activ_dep = 0
    c_activ_pnfp = 0
    c_activ_rro = 0
    c_noactiv_rro = 0
    c_own = 0
    c_noown = 0
    c_allrro = 0

    out_text = 'партнёр;отделений;ПНФП;активн отделения;активн ПНФП;актив РРО;неактивн РРО;свои;аренда;всего;возврат\n'
    for partner in partners:
        line = f'{partner};'
        
        u = get_line(q_dep, partner)
        c_dep += int(u)
        line += u + ';'
        
        u = get_line(q_pnfp, partner)
        c_pnfp += int(u)
        line += u + ';'


        u = get_line(q_activ_dep, partner)
        c_activ_dep += int(u)
        line += u + ';'

        u = get_line(q_activ_pnfp, partner)
        c_activ_pnfp += int(u)
        line += u + ';'


        u = get_line(q_activ_rro, partner)
        c_activ_rro += int(u)
        line += u + ';'
        
        u = get_line(q_noactiv_rro, partner)
        c_noactiv_rro += int(u)
        line += u + ';'

        u = get_line(q_own, partner)
        c_own += int(u)
        line += u + ';'
        
        u = get_line(q_noown, partner)
        c_noown += int(u)
        line += u + ';'
        
        
        u = get_line(q_allrro, partner)
        c_allrro += int(u)
        line += u + ';'
        
        out_text += line + '\n'

    out_text += f'всего:;{c_dep};{c_pnfp};{c_activ_dep};{c_activ_pnfp};{c_activ_rro};{c_noactiv_rro};{c_own};{c_noown};{c_allrro};'
    
    data = mk_data()

    out_text += '\n________________\n'
    out_text += 'партнёр;терминал;отделение;ЗН;ФН;статус;область;город;адрес;едрпоу\n'
    
    for line in data:
        out_text += ';'.join(line) + '\n'
    
    
    
    out_fname = OUT_DATA_PATH + 'DOC/' + 'Ekv.csv'
    text_to_file(out_text, out_fname)
    #save_and_show(out_text, out_fname)

    return inf + out_text + '\n\n' + out_fname



sign_active = 'Активний'
sign_noactive = 'Заблокований'
sign_priostanov = 'Призупинений'

#print(main())
#print(sum_activ_pnfp())