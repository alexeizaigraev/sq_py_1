import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import sqlite3
from datetime import datetime


def get_con():
    con = sqlite3.connect(DB_PATH)
    return con


def db_exec(query):
    con = get_con()
    cur = con.cursor()
    rez = cur.execute(query)
    con.commit()
    con.close()
    return str(rez)


def db_exec_one(sql, vec):
    vec = good_vec(vec)
    con = get_con()
    cur = con.cursor()
    rez = cur.execute(sql, vec)
    con.commit()
    con.close()
    return str(rez)


def db_exec_many(sql, arr):
    con = get_con()
    cur = con.cursor()
    rez = cur.executemany(sql, arr)
    con.commit()
    con.close()
    return str(rez)


def get_one_data(query):
    con = get_con()
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchone()
    con.close()
    return data


def get_data(query):
    con = get_con()
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    con.close()
    return data


def get_list(query):
    arr = []
    rows = get_data(query)
    for line in rows:
        if line[0]:
            arr.append(line[0])
    return arr

            
def clear_table(table):
    db_exec(f'DELETE FROM {table}')

def vec_to_query(vec):
    for i in range(len(vec)):
        vec[i] = f"'{vec[i]}'"
    return ','.join(vec)

def refresh_table_papa(table_name, fname, flag_lite=True):
    my_list = []
    if table_name == 'departments':
        columns = COL_DEPS
        if flag_lite:
            my_list = get_list('SELECT department FROM departments')
    elif table_name == 'terminals':
        columns = COL_TERMS
        if flag_lite:
            my_list = get_list('SELECT termial FROM terminals')
    elif table_name == 'otbor':
        columns = COL_OTBORS
    elif table_name == 'koatu_spr':
        columns = COL_KOATU_SPRS
    elif table_name == 'ekv':
        columns = COL_EKVS
    elif table_name == 'comon_data':
        columns = COL_COMON_DATAS
    
    if not flag_lite:
        clear_table(table_name)
    info = ''
    count = 0
    q_err = 0
    arr = file_to_arr_nosharp(fname)[1:]
    con = get_con()
    cur = con.cursor()
    for vec in arr:
        vec =  good_vec(vec)
        if flag_lite and my_list:
            if table_name == 'departments':
                if vec[0] in my_list:
                    info += f'pass {vec[0]}\n'
                    continue
            if table_name == 'terminals':
                if vec[1] in my_list:
                    info += f'pass {vec[1]}\n'
                    continue
        query = f'''INSERT INTO {table_name} (
            {columns}
            )
            VALUES ({vec_to_query(vec)});'''
        try:
            cur.execute(query)
            #con.commit()
            count += 1 
        except Exception as ex:
            info += str(ex) + '\n'
            info += f'{vec[0]};{vec[1]}\n'
            q_err += 1
    con.commit()
    if con:
        cur.close()
        con.close()
    if q_err == 0:
        info += f'success refresh {count=} {table_name}\n\n'
    else:
        info += f'{q_err=} {count=} refresh {table_name}\n\n'
    return info


def table_to_file_papa(tname, fname):
    info = ''
    if tname == 'departments':
        text = 'department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner_name;id_terminal;koatu;tax_id;koatu2\n'
    elif tname == 'terminals':
        text = 'department;termial;model;serial_number;date_manufacture;soft;producer;rne_rro;sealing;fiscal_number;oro_serial;oro_number;ticket_serial;ticket_1sheet;ticket_number;sending;books_arhiv;tickets_arhiv;to_rro;owner_rro;register;finish\n'
    elif tname == 'ekv':
        text = 'fiscal;status\n'

    rows = get_data(f'SELECT * FROM {tname};')

    for vec in rows:
        text += ';'.join(vec) + '\n'
    text_to_file(text, fname)
    info += fname + '\n'
    return info

def date_log():
    ddd = datetime.now().date()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{y}.{m}.{d}'


COL_DEPS = 'department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2'
COL_TERMS = 'department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish'
COL_OTBORS = 'term, dep'
COL_KOATU_SPRS = 'koatu2, koatu_old, place'
COL_EKVS = 'fiscal, status'
COL_COMON_DATAS = 'partner, code, kass_owner, email, gdrive, regime, term_owner, term_shablon, soft_version, limit_kass'

DB_PATH = f'{DATA_PATH}db/drm.db'
