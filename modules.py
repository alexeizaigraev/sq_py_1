# -*- coding: utf-8 -*-
""" Набор модулей """
import os
import shutil
from pathlib import Path
import datetime
from sys import platform
import subprocess


from colorama import Fore, Style, init


# def my_clear():
#     if platform == 'linux':
#         os.system('clear')
#     else:
#         os.system('cls')

# def sos(err, fact):
#     """Сообщение об ошибке - запрос ввода - меню"""
#     print('>> Err ', err, fact)
#     input('## Press Any Key')
#     input()
#     os.system(PYTHON_NAME + ' main.py')

# def alarm(err, fact):
#     """Сообщение об ошибке - без прерывания программы"""
#     print('>> Err ', err, fact)

def sharp_nobom_file(path):
    #app_path = file_to_arr_nosharp('Config/SharpNoBomPath.txt')[0]
    subprocess.run(f'CSharpNoBom/NoBom.exe {path}')
    

def file_to_arr(path):
    """ Читает файл в массив. имя файла: path """
    sharp_nobom_file(path)
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            if ";" in line:
              b.append(line.strip().split(";"))
            else:
               b.append(line.strip())
    return b

def file_to_arr_nosharp(path):
    """ Читает файл в массив. имя файла: path """
    #sharp_nobom_file(path)
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            if ";" in line:
              b.append(line.strip().split(";"))
            else:
               b.append(line.strip())
    return b



def file_to_gen(path):
    """ Читает файл в массив. имя файла: path """
    sharp_nobom_file(path)
    for line in open(path, 'r', encoding="UTF-8"):
        if ";" in line:
            b = line.strip().split(";")
        else:
            b = line.strip()
        yield b

def file_to_vec_nosharp(path):
    """ Читает файл в массив. имя файла: path """
    #sharp_nobom_file(path)
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            b.append(line.strip())
    return b

def file_to_vec(path):
    """ Читает файл в массив. имя файла: path """
    sharp_nobom_file(path)
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            b.append(line.strip())
    return b

def file_to_dict_one(fname, num_col):
    sharp_nobom_file(fname)
    h = dict()
    with open(fname, 'r', encoding="UTF-8") as file:
        for line in file:
            split_line = line.strip().split(";")
            h[split_line[0]] = split_line[num_col]
    return h


def arr_to_text(arr):
    text = ''
    for v in arr:
        text += ';'.join(v) + "\n"
    return text

def file_to_text(fname):
    sharp_nobom_file(fname)
    text = None
    with open(fname, 'r', encoding="UTF-8") as file:
        text = file.read()
    return text

def file_to_text_nosharp(fname):
    #sharp_nobom_file(fname)
    text = None
    with open(fname, 'r', encoding="UTF-8") as file:
        text = file.read()
    return text

def text_to_file(b, fname):
    info = ''
    """Записывает текст b в файл с именем fname"""
    with open(fname, 'w', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        info += f'emptty {fname}\n'
    else:
        info += f'\n {fname}\n'
    return info

def text_add_file(b, fname):
    info = ''
    """Записывает текст b в файл с именем fname"""
    with open(fname, 'a', encoding="UTF-8") as out_object:
        out_object.write(b)

    if b == '':
        info += f'clear {fname}\n'
    else:
        info += f'\n\t add to: {fname}\n'
    return info

def save_and_show(text, fname):
    info = text_to_file(text, fname)
    open_name = 'notepad.exe ' + fname
    os.system(open_name)
    return info

def open_note(fname):
    open_name = 'notepad.exe ' + fname
    os.system(open_name)


def arr_to_file(b, fname):
    """Записывает массив b в файл с именем fname"""
    with open(fname, 'w', encoding="UTF-8") as file:
        for bb in b:
            file.write(";".join(bb) + "\n")
    return f'\n\t{fname}\n'


def text_to_file_cp1251(b, fname):
    """Записывает text b в файл с именем fname"""
    with open(fname, 'w', encoding="cp1251") as file:
        file.write(b)
    return fname

def now_date_normal():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{d}.{m}.{y}'

def now_date_kabinet():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{d}{m}{y}'

def now_date_log():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{d}.{m}.{y}'


def now_date_line_revers():
    ddd = datetime.date.today()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{y}-{m}-{d}'

def mk_natasha():
    sign = 'Відділення № '
    #b = ['1', '1330523', '1330524', '1330528',]
    b = []
    with open(IN_DATA_PATH + 'natasha.csv', 'r', encoding="UTF-8") as file:
        for line_str in file:
            line = line_str.strip().split(';')
            for unit in line:
                if sign in unit:
                    el = unit.replace(sign, '').strip()
                    b.append(el)
    return set(b)


# перепиливаем
def comon_data_list0(col_num):
    rez = []
    with open(COMON_DATA_PATH, 'r', encoding="UTF-8") as file:
        for line in file:
            vec = line.split(';')
            if 'nodata' not in vec[col_num]:
                rez.append(vec[col_num])
    return rez

def dir_kabinet(self):
        return file_to_arr_nosharp(CONFIG_PATH + 'ConfigKabinetPath.txt')[0]


def mover(old_name, new_name):
    info = ''
    try:
        shutil.move(old_name, new_name)
        info += new_name + '\n'
    except:
        info += f'>> err {old_name}\n'
    return info

def coper(old_name, new_name):
    info = ''
    try:
        shutil.copy(old_name, new_name)
        info += new_name + '\n'
    except:
        info += f'>> err {old_name}'
    return info

def good_vec(vec):
    for i in range(len(vec)):
        vec[i] = vec[i].strip().replace("'", "`").replace('"','').replace('\n', '')
    return vec

"""

def p_red(text):
    init()
    print(Fore.RED + text)
def p_green(text):
    init()
    print(Fore.GREEN + text)
def p_yellow(text):
    init()
    print(Fore.YELLOW + text)
def p_cyan(text):
    init()
    print(Fore.CYAN + text)
def p_magenta(text):
    init()
    print(Fore.MAGENTA + text)
def p_blue(text):
    init()
    print(Fore.LIGHTBLUE_EX + text)


def ask(vec):
    os.system(COM_CLEAR)
    print('\n\n')
    for i in range(len(vec)):
        p_green(f'\t{i} {vec[i]}')

    print('\n\n\t-> ', end = '')
    choise = input()
    return vec[int(choise)]

"""
#koatu-new_______________

def niseStr(str):
    return str.replace("’", '').replace("'", '').replace(' ', '').replace('-', '').replace('`', '').lower()


def strInBoth(str1, str2):
    str1 = niseStr(str1)
    str2 = niseStr(str2)
    if ( str1 in str2 ) or ( str2 in str1 ):
        return True
    return False




#end_koatu_new___________


DATA_PATH = file_to_arr_nosharp('Config/ConfigDataPath.txt')[0]
IN_DATA_PATH = DATA_PATH + 'InData/'
OUT_DATA_PATH = DATA_PATH + 'OutData/'
CONFIG_PATH = DATA_PATH + 'Config/'
#COMON_DATA_PATH = CONFIG_PATH + 'comon_data.csv'
CONFIG_DIR_PATH = DATA_PATH + 'ConfigDir/'

KABINET_DIR = file_to_arr_nosharp(CONFIG_PATH + 'ConfigKabinetPath.txt')[0]
#KABINET_DIR = 'G:/Мой диск/DRM/KABINET/'
#KABINET_DIR = 'C:/Users/Alex/Desktop/ЯРЛЫКИ/Data/Kabinet/'

KABINET_DIR_R = 'R:/DRM/Ключи/КНИГИ/'

GDRIVE_PATH = 'G:/Мой диск/'
GDRIVE_BACKUP_PATH = GDRIVE_PATH + 'PG_BACKUP/'

#PG_BACKUP_PATH = 'R:/DRM/BackupAccess/'
PG_BACKUP_PATH = GDRIVE_BACKUP_PATH
SQ_BACKUP_PATH = 'G:/Мой диск/DRM/SQ_LITE/'
#PG_BACKUP_PATH = 'C:/PgBackUp/'

if platform == 'linux':
    py_prefix = 'python3'
    com_clear = 'clear'
else:
    py_prefix = 'python'
    com_clear = 'cls'

COM_CLEAR = com_clear
PYTHON_NAME = py_prefix


#koatuSpr = file_to_arr_nosharp(IN_DATA_PATH + 'koatuall.csv')
lb_status = 'term'
