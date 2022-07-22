import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from db.db_base import *
from modules import *


def ekv_from_gdrive():
    return refresh_table_papa('ekv', PG_BACKUP_PATH + 'ekv.csv', False)


def ekv_from_indata_full():
    return refresh_table_papa('ekv', IN_DATA_PATH + 'ekv.csv', False)


def refresh_one_ekv(vec):
    try:
        query = f"""UPDATE terminals
SET tickets_arhiv = '{vec[1]}'
WHERE terminals.fiscal_number = '{vec[0]}';"""
    except:
        pass
    db_exec(query)
