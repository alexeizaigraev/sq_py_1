from db.db_base import *
from db.db_dep import *
from db.db_term import *
from db.db_ekv import *
from db.db_comon_data import *
from db.db_koatu_spr import *
from db.db_otbor import *


def refresh_koatu_spr():
    return refresh_table_papa('koatu_spr', koatu_spr_path, False)


def refresh_comon_data():
    return refresh_table_papa('comon_data', comon_data_path, False)



def refresh_2():
    print(refresh_koatu_spr())
    print(refresh_comon_data())
    print('well')

comon_data_path = 'D:/data/comon_data.csv'
koatu_spr_path = f'{IN_DATA_PATH}koatuall.csv'

#refresh_2()
