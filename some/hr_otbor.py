import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

def get_summury_otbor_data():
    query = f'''SELECT department, region, district_region, post_index, city_type, city, district_city, street_type, street, hous, address, koatu, koatu2
FROM departments, otbor
WHERE department = dep
ORDER BY department;'''
    return get_data(query)

def niseStr(str):
    return str.replace("’", '').replace("'", '').replace(' ', '').replace('-', '').replace('`', '').lower() 


def strInBoth(str1, str2):
    str1 = niseStr(str1)
    str2 = niseStr(str2)
    if ( str1 in str2 ) or ( str2 in str1 ):
        return True
    return False


def mk_koatu2(koatuSpr, sity, distrSity, koatu):
    if not koatu:
        return ''
    for line in koatuSpr:
        sprKoatu = line[1]
        sprPlace = line[2]
        if (koatu in sprKoatu or sprKoatu in koatu) \
        and ( strInBoth(sprPlace, sity) or ( strInBoth(sprPlace, distrSity) ) ):
            return line[0]
    return ''

def main():

    info = ''
    koatuSpr = file_to_arr_nosharp(IN_DATA_PATH + 'koatuall.csv')

    head = '№ п/п;"№ Відділення ТОВ ""ЕПС""";Область;Район в обл.;Індекс;Тип населеного пункту;Населений пункт;Район в місті;Тип вулиці;Адреса;Номер будинку;Дата признчення керівника;модель РРО;Заводський № РРО;2;koatu1;koatu2\n'
    out_text = head

    data = get_summury_otbor_data()

    my_deps = []
    count = 0
    for line in data:
        line = list(line)
        sity = line[5]
        distrSity = line[6]
        koatu = line[11]
        koatu2 = ''
        q = f"""SELECT koatu2
        FROM koatu_spr
        WHERE koatu_old = '{koatu}'
        AND
        (place = '{sity}'
        OR place = '{distrSity}');"""
        try:
            koatu2 = get_list(q)[0]
        except:
            pass
        adrFull = line[12]

        line[-1] = koatu2
        
        line = list(line)
        
        dep = line[0]
        if not dep:
            continue
        count += 1
        out_line = (str(count) + ';' 
                + line[0]  + ';'
                + line[1] + ';'
                + line[2] + ';'
                + line[3] + ';'
                + line[4] + ';'
                + line[5] + ';'
                + line[6] + ';'
                + line[7] + ';'
                + line[8] + ';'
                + line[9] + ';'
                + '' + ';'
                + '' + ';'
                + '' + ';'
                + line[10] + ';'
                + line[11] + ';'
                + line[12] )
        out_text += out_line + '\n'
        info += f'{line[0]} {koatu2}\n'
        

    info += text_to_file(out_text, OUT_DATA_PATH + 'hr_new_deps.csv')
    return info

