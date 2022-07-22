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

#otbor = get_otbor_deps()
otbor = """1330054
1330062
1330064
1330066
1330081
1330104
1330105
1330115
1330159
1330169
1330172
1330176
1330197
1330207
1330211
1330220
1330221
1330230
1330249
1330257
1330274
1330290
1330311
1330323
1330340
1330342
1330349
1330363
1330366
1330379
1330399
1330400
1330410
1330417
1330427
1330430
1330435
1330444
1330447
1330448
1330453
1330454
1330472
1330473
1330476
1330478
1330482
1330485
1330491
1330496
1330499
1330504
1330507
1330514
1330516
1330519
1330520
1330540
1330547
1330551
1330556
1330561
1330574
1330582
1330433
1330522
1330525
1330526
1330527
1330529
1330529
1330530
1330531
""".split('\n')
for otbor_dep in otbor:
    key = otbor_dep[:3]
    try:
        folder = dict_folder[key]
    except Exception as ex:
        print(str(ex))
        continue
    path_folder = GDRIVE_PATH + '/' + folder + '/' + otbor_dep
    files = os.listdir(path_folder)
    for fname in files:
        if 'RP' in fname:
            old_path = f'{path_folder}/{fname}'
            new_path = f'{KABINET_DIR}{fname}'
            shutil.copyfile(old_path, new_path)
            sum += 1
            print(new_path)

print(f'\n{sum=}\n')
