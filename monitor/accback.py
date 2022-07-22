# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import os
import shutil
from pathlib import Path
from modules import *
from datetime import datetime
import shutil

from papa_pg import *

def accback():
    #info = ''
    new_fname = f'{SQ_BACKUP_PATH}{now_date_line_revers()}_drm.db'
    old_fname = f'{DATA_PATH}db/drm.db'

    try:
        shutil.copy(old_fname, new_fname)
        return new_fname
    except Exception as ex:
        return f'{ex}'
    

    #info += select_deps_to_gdrive()
    #info += select_terms_to_gdrive()

    #info += select_deps_to_gdrive_log()
    #info += select_terms_to_gdrive_log()

    #return info

#print(accback())
#print(select_deps_to_gdrive())

        