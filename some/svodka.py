# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
from papa_pg import *

def arr_to_text(arr):
    txt = ''
    for line in arr:
        txt += f'{line[0]};{line[1]}\n'
    return txt

def all_term():
    head = '\n\nвсего терминалы\nпартнёр;кол-во терм\n'
    q = """SELECT ddd.partner, COUNT(ttt.termial)
FROM departments ddd
LEFT OUTER JOIN terminals ttt
ON ddd.department = ttt.department
GROUP BY ddd.partner
ORDER BY ddd.partner"""
    return head + arr_to_text(get_data(q)) 

def term_on_dep():
    head = '\n\nотделения\nпартнёр;кол-во терм\n'
    q = """SELECT ddd.partner, COUNT(ttt.termial)
FROM departments ddd
LEFT OUTER JOIN terminals ttt
ON ddd.department = ttt.department
WHERE ddd.edrpou !='' 
GROUP BY ddd.partner
ORDER BY ddd.partner"""
    return head + arr_to_text(get_data(q)) 

def term_on_pnfp():
    head = '\n\nПНФП\nпартнёр;кол-во терм\n'
    q = """SELECT ddd.partner, COUNT(ttt.termial)
FROM departments ddd
LEFT OUTER JOIN terminals ttt
ON ddd.department = ttt.department
WHERE ddd.edrpou ='' 
GROUP BY ddd.partner
ORDER BY ddd.partner"""
    return head + arr_to_text(get_data(q)) 

def main():
    out = ''
    out += all_term()
    out += term_on_dep()
    out += term_on_pnfp()
    return out

print(main())