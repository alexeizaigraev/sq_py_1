import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from db.db_base import * 

def comon_data_dict_db(col_key_num):
    h = dict()
    for line in get_data('SELECT * FROM comon_data;'):
        h[line[1]] = line[col_key_num]
    return h

