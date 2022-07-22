import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 
from modules import *
from db.db_base import *


def refresh_otbor_from_indata():
    return refresh_table_papa('otbor', IN_DATA_PATH + 'otbor.csv', False)


def insert_all_otbor(arr):
    clear_table('otbor')
    info = ''
    count = 0
    q_err = 0
    con = get_con()
    cur = con.cursor()
    for vec in arr:
        #vec =  good_vec(vec)
        query = f''' INSERT INTO otbor (term, dep)
VALUES ('{vec[0]}', '{vec[1]}')'''
        try:
            cur.execute(query)
            count += 1 
        except Exception as ex:
            info += str(ex) + '\n'
            q_err += 1
    con.commit()
    if con:
        cur.close()
        con.close()
    if q_err == 0:
        info += f'success refresh {count=} otbor\n\n'
    else:
        info += f'\t{q_err=} {count=} refresh otbor\n\n'
    return info


def get_otbor_deps():
    query = f'''SELECT dep FROM otbor
ORDER BY dep'''
    return get_list(query)


