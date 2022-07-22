# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
from papa_pg import *

def data_to_text(arr):
    b = []
    for line in arr:
        vec = list(line)
        vec[-1] = str(vec[-1])
        b.append(vec)
    return b

def mk_full_data0():
    q = """
    SELECT d.partner, t.tickets_arhiv, t.owner_rro, count(*  )
FROM departments d, terminals t
WHERE d.department = t.department
AND t.tickets_arhiv IS NOT NULL
AND t.tickets_arhiv != ''
GROUP BY (d.partner, t.tickets_arhiv, t.owner_rro)
ORDER BY d.partner, t.tickets_arhiv, t.owner_rro;
"""
    return get_data(q)


def mk_full_data():
    q = """
    SELECT d.partner, t.tickets_arhiv, t.owner_rro, t.sealing, count(*  )
FROM departments d, terminals t
WHERE d.department = t.department
AND t.tickets_arhiv IS NOT NULL
AND t.tickets_arhiv != ''
GROUP BY d.partner, t.tickets_arhiv, t.owner_rro, t.sealing
ORDER BY d.partner, t.tickets_arhiv, t.owner_rro, t.sealing;
"""
    return get_data(q)



def mk_data():
    q = """
    SELECT departments.partner,
	terminals.termial, terminals.department,
	terminals.serial_number, terminals.fiscal_number,
	terminals.tickets_arhiv, terminals.owner_rro,
    terminals.sealing,
	departments.region, departments.city, departments.address,
    departments.edrpou
FROM terminals, departments
WHERE departments.department = terminals.department
ORDER BY terminals.termial
"""
    return get_data(q)

def mk_partners(data):
    vec = []
    for line in data:
        vec.append(line[0])
    return vec

def analis(data, col):
    h = dict()
    variants = []
    for line in data:
        variants.append(line[col])

    for variant in variants:
        h[variant] = 0
        for line in data:
            if variant == line[col]:
                h[variant] += line[-1]
        for key in h:
            h[key] = str(h[key])
    return h




def main():
    inf = 'партнёр;статус;собственник;аренда;количество\n'
    data0 = mk_full_data()
    data = data_to_text(data0)
    
    
    for line in data:
        inf += ';'.join(line) + '\n'

    out_text = inf
    
    for i in range(len(data0[0])-1):
        inf += '\n________________\n' 
        if i == 0:
            inf += 'патнёр\n'
        if i == 1:
            inf += 'статус\n'
        if i == 2:
            inf += 'собственник\n'
        if i == 3:
            inf += 'аренда\n'
        u = analis(data0, i)
        for u_key in u:
            inf += f'{u_key};{u[u_key]}\n'
        
    data = mk_data()

    inf += '\n________________\n'


    #out_text += '\n________________\n'
    inf += 'партнёр;терминал;отделение;ЗН;ФН;статус;собственник;аренда;область;город;адрес;едрпоу\n'
    
    for line in data:
        inf += ';'.join(line) + '\n'

    
    out_fname = OUT_DATA_PATH + 'DOC/' + 'EkvGroup.csv'
    text_to_file(inf, out_fname)
    #save_and_show(out_text, out_fname)

    #print(inf)

    return out_fname + '\n\n' + inf

