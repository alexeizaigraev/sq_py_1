import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from db.db_base import *
from modules import *


def tickets_arhiv_update():
    q = """UPDATE terminals
SET tickets_arhiv = ekv.status
FROM ekv
WHERE terminals.fiscal_number = ekv.fiscal;"""
    db_exec(q)
    return '\ntickets_arhiv udate\n'

#_______________________________________

def refresh_terms_from_indata():
    return refresh_table_papa('terminals', IN_DATA_PATH + 'terminals.csv', False)


def refresh_terms_from_gdrive():
    return refresh_table_papa('terminals', PG_BACKUP_PATH + 'terminals.csv', False)


def refresh_terms_from_indata_lite():
    return refresh_table_papa('terminals', IN_DATA_PATH + 'terminals.csv', True)

#_______________________________________

def select_terms_to_indata():
    return table_to_file_papa('terminals', IN_DATA_PATH + 'terminals.csv')

def select_terms_to_gdrive():
    return table_to_file_papa('terminals', PG_BACKUP_PATH + 'terminals.csv')

def select_terms_to_gdrive_log():
    return table_to_file_papa('terminals', f'{PG_BACKUP_PATH}{date_log()}_terminals.csv')

#_______________________________________



def get_address(dep):
    query = f"select address from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0][0]


def get_tax_id(dep):
    query = f"select tax_id from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0]
    

def get_terminals_list():
    query = f'''SELECT termial FROM terminals
ORDER BY termial'''
    return get_list(query)

def get_terminals_list_partner(partner):
    query = f'''SELECT termial FROM terminals, departments
    WHERE departments.department = terminals.department
    AND departments.partner = '{partner}'
ORDER BY termial;'''
    return get_list(query)


def get_model_list():
    query = f'''SELECT DISTINCT model FROM terminals
ORDER BY model'''
    return get_list(query)

def get_owners():
    vec = ['',]
    query = 'SELECT DISTINCT owner_rro FROM terminals ORDER BY owner_rro'
    return vec + get_list(query)

def get_models():
    vec = ['',]
    query = 'SELECT DISTINCT model FROM terminals ORDER BY model'
    return vec + get_list(query)

def get_softs():
    vec = ['',]
    query = 'SELECT DISTINCT soft FROM terminals ORDER BY soft DESC'
    return vec + get_list(query)

def get_seals():
    vec = ['',]
    query = 'SELECT DISTINCT sealing FROM terminals ORDER BY sealing DESC'
    return vec + get_list(query)


def get_ekv_fiscal_activ():
    query = """SELECT DISTINCT fiscal_number FROM terminals
    WHERE tickets_arhiv = 'Активний';"""
    return get_list(query)

def get_ekv_fiscal_blocked():
    query = """SELECT DISTINCT fiscal_number FROM terminals
    WHERE tickets_arhiv != 'Активний';"""
    return get_list(query)


def get_one_term_data(term):
    query = f'''SELECT * 
FROM terminals
WHERE terminals.termial = '{term}';'''
    return get_data(query)



def del_term(key):
    q=f"""DELETE FROM terminals
	WHERE termial = '{key}';
    """
    db_exec(q)


def refresh_one_term(vec):
    vec = good_vec(vec)
    info = ''
    try:
        del_term(vec[1])
    except:
        pass
    query = f'''INSERT INTO terminals(
	department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish)
	VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}', '{vec[19]}', '{vec[20]}', '{vec[21]}');'''
    db_exec(query)

# navi __________________

def next_term(term):
    vec = get_terminals_list()
    if term in vec:
        if vec.index(term) < len(vec) - 1:
            return vec[vec.index(term) + 1]
        else:
            return vec[0] 


def pred_term(term):
    vec = get_terminals_list()
    if term in vec:
        if vec.index(term) > 0:
            return vec[vec.index(term) - 1]
        else:
            return vec[len(vec) -1]


 # ______________________ 


def get_serial_list():
    query = f'''SELECT DISTINCT serial_number FROM terminals
ORDER BY serial_number'''
    return get_list(query)


def get_fiscal_list():
    query = f'''SELECT DISTINCT fiscal_number FROM terminals
ORDER BY fiscal_number'''
    return get_list(query)


def get_status_list():
    out = ['',]
    query = f'''SELECT DISTINCT tickets_arhiv FROM terminals
ORDER BY tickets_arhiv'''
    return out + get_list(query)

def find_term_on_fiscal(fiscal):
    q = f"""SELECT termial 
    FROM terminals
    WHERE fiscal_number LIKE '%{fiscal}';"""
    try:
        return get_data(q)[0][0]
    except:
        return ''

def find_term_on_serial(serial):
    q = f"""SELECT termial 
    FROM terminals
    WHERE serial_number LIKE '%{serial}';"""
    try:
        return get_data(q)[0][0]
    except:
        return ''

