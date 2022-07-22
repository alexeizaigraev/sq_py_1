import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 
from db.db_base import *
from modules import *

def mk_koatu2(sity, distrSity, koatu):
    koatu2 = ''
    q = f"""SELECT koatu2
    FROM koatu_spr
    WHERE koatu_old = '{koatu}'
    AND (
    place = '{sity}'
    OR place = '{distrSity}'
    );"""
    try:
        return get_list(q)[0] 
    except:
        return  ''
    
    

