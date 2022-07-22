import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from db.db_base import *


def refresh_deps_from_indata():
    return refresh_table_papa('departments', IN_DATA_PATH + 'departments.csv', False)


def refresh_deps_from_gdrive():
    return refresh_table_papa('departments', PG_BACKUP_PATH + 'departments.csv', False)


def refresh_deps_from_indata_lite():
    return refresh_table_papa('departments', IN_DATA_PATH + 'departments.csv', True)

#_______________________________________

def select_deps_to_indata():
    return table_to_file_papa('departments', IN_DATA_PATH + 'departments.csv')

def select_deps_to_gdrive():
    return table_to_file_papa('departments', PG_BACKUP_PATH + 'departments.csv')

def select_deps_to_gdrive_log():
    return table_to_file_papa('departments', f'{PG_BACKUP_PATH}{date_log()}_departments.csv')

#_______________________________________


def get_partners():
    query = f'''SELECT DISTINCT partner
FROM departments
ORDER BY partner;'''
    return get_list(query)


def get_departments_list():
    query = f'''SELECT department FROM departments
ORDER BY department'''
    return get_list(query)



def get_city_types():
    vec = ['',]
    query = 'SELECT DISTINCT city_type FROM departments ORDER BY city_type'
    return vec + get_list(query)

def get_street_types():
    vec = ['',]
    query = 'SELECT DISTINCT street_type FROM departments ORDER BY street_type'
    return vec + get_list(query)

def get_one_dep_data(dep):
    query = f'''SELECT * 
FROM departments
WHERE departments.department = '{dep}';'''
    return get_data(query)[0]


#_________

def del_dep(dep):
    q=f"""DELETE FROM public.departments
	WHERE department = '{dep}';
    """
    db_exec(q)


  
def add_one_dep(vec):
    vec = good_vec(vec)
    info = ''
    vec.append('')
    try:
        del_dep(vec[0])
    except:
        pass
    query = f"""INSERT INTO departments ({COL_DEPS})
    VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}' , '{vec[19]}');"""
    db_exec(query)

def edit_update(data):
    q = f"""UPDATE departments SET
    region = '{data[1]}',
    district_region = '{data[2]}',
    district_city = '{data[3]}',
    city_type = '{data[4]}',
    city = '{data[5]}',
    street = '{data[6]}',
    street_type = '{data[7]}',
    hous = '{data[8]}',
    post_index = '{data[9]}',
    partner = '{data[10]}',
    status = '{data[11]}',
    register = '{data[12]}',
    edrpou = '{data[13]}',
    address = '{data[14]}',
    partner_name = '{data[15]}',
    id_terminal = '{data[16]}',
    koatu = '{data[17]}',
    tax_id = '{data[18]}',
    koatu2 = '{data[19]}'
    WHERE department = '{data[0]}'
    ;"""
    try:
        db_exec(q)
        return f'update {data[0]}'
    except Exception as ex:
        return str(ex)

# navi _____________________________

  
def next_dep(dep):
    vec = get_departments_list()
    if dep in vec:
        if vec.index(dep) < len(vec) - 1:
            return vec[vec.index(dep) + 1]
        else:
            return vec[0]
    else:
        return(str(vec))

def pred_dep(dep):
    vec = get_departments_list()
    if dep in vec:
        if vec.index(dep) > 0:
            return vec[vec.index(dep) - 1]
        else:
            return vec[len(vec) -1]

# ________________________________

def get_koatu(dep):
    query = f"select koatu from departments WHERE department = '{dep}'"
    arr = get_data(query)
    return arr[0]

def get_koatu2(dep):
    query = f"select city, district_city, koatu from departments WHERE department = '{dep}';"
    vec = get_data(query)[0]
    city = vec[0].strip()
    distrCity = vec[1].strip()
    koatu = vec[2].strip()
    if not city:
        city = ''
    if not distrCity:
        distrCity = ''
    if not koatu:
        koatu = ''
    rez = ""
    try:
        from db.db_koatu_spr import mk_koatu2
        rez = mk_koatu2(city, distrCity, koatu)
    except:
        pass
    return rez



