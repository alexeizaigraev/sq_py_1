# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
from papa_pg import get_otbor_deps, comon_data_dict_db


init()
sum = 0

out_path = KABINET_DIR
old = os.listdir(out_path)
for fname in old:
    try:
        if '.pdf' in fname:
            os.remove(out_path + fname)
    except:
        print('err remove', fname)


dict_folder = comon_data_dict_db(4)

otbor = get_otbor_deps()
for otbor_dep in otbor:
    key = otbor_dep[:3]
    try:
        folder = dict_folder[key]
    except Exception as ex:
        p_red(str(ex))
        continue
    path_folder = GDRIVE_PATH + '/' + folder + '/' + otbor_dep
    files = os.listdir(path_folder)
    for fname in files:
        if 'RP' in fname:
            old_path = f'{path_folder}/{fname}'
            new_path = f'{KABINET_DIR}{fname}'
            shutil.copyfile(old_path, new_path)
            sum += 1
            p_cyan(new_path)

p_green(f'\n{sum=}\n')
