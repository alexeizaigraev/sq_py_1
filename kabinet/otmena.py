import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, mk_koatu2


def get_kabinet_otmena_data():
    query = '''SELECT terminals.ticket_number, terminals.serial_number,
terminals.model, terminals.soft, terminals.rne_rro, 
departments.address, departments.koatu, departments.tax_id,
terminals.fiscal_number, departments.department
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)


def main():

    info = ''
    data = get_kabinet_otmena_data()

    for u in data:
        shablon =f"""<?xml version="1.0" encoding="windows-1251" standalone="no"?>
    <DECLAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="J1313602.xsd">
        <DECLARHEAD>
            <TIN>40243180</TIN>
            <C_DOC>J13</C_DOC>
            <C_DOC_SUB>136</C_DOC_SUB>
            <C_DOC_VER>2</C_DOC_VER>
            <C_DOC_TYPE>0</C_DOC_TYPE>
            <C_DOC_CNT>541</C_DOC_CNT>
            <C_REG>26</C_REG>
            <C_RAJ>50</C_RAJ>
            <PERIOD_MONTH>5</PERIOD_MONTH>
            <PERIOD_TYPE>1</PERIOD_TYPE>
            <PERIOD_YEAR>2020</PERIOD_YEAR>
            <C_STI_ORIG>2650</C_STI_ORIG>
            <C_DOC_STAN>1</C_DOC_STAN>
            <LINKED_DOCS xsi:nil="true"/>
            <D_FILL>17052020</D_FILL>
            <SOFTWARE>CABINET</SOFTWARE>
        </DECLARHEAD>
    <DECLARBODY>
    <HKSTI>2650</HKSTI>
    <HSTI>ГОЛОВНЕ УПРАВЛІННЯ ДФС У М.КИЄВІ, ДПІ У ГОЛОСІЇВСЬКОМУ РАЙОНІ (ГОЛОСІЇВСЬКИЙ РАЙОН М.КИЄВА)</HSTI>
    <HNAME>ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ "ЕЛЕКТРУМ ПЕЙМЕНТ СІСТЕМ"</HNAME>
    <HTIN>40243180</HTIN>
    <R001G1S>{u[8]}</R001G1S>
    <R002G1S>{u[1]}</R002G1S>
    <R003G1>420</R003G1>
    <R003G1S>{u[2]}</R003G1S>
    <R004G1>1085</R004G1>
    <R004G1S>{u[3]}</R004G1S>
    <R007G1S>{u[4]}</R007G1S>
    <R008G1S>{u[5]}</R008G1S>
    <R009G1>{u[6]}</R009G1>
    <R010G1S>{u[7]}</R010G1S>
    <R011G1S>закриття відділення</R011G1S>
    <R012G1S>{u[8]}</R012G1S>
    <M03>1</M03>
    <M04>1</M04>
    <HKBOS>2903722436</HKBOS>
    <HBOS>ПОЖАРСЬКИЙ ВЯЧЕСЛАВ ЮХИМОВИЧ</HBOS>
    <HFILL>{now_date_kabinet()}</HFILL>
    <HZ>1</HZ>
        <HZM>2</HZM>
        <HMONTH>2</HMONTH>
        <HZY>2020</HZY>
    </DECLARBODY>
    </DECLAR>"""

        try:
            ofname = KABINET_DIR + u[-1] +'_otmena_' + u[-2] + '_' + u[1] + '.xml'
            #print(ofname)
            text_to_file_cp1251(shablon, ofname)
            info += ofname + '\n'
        except:
            pass

        try:
            ofname = KABINET_DIR_R + u[-1] +'_otmena_' + u[-2] + '_' + u[1] + '.xml'
            #print(ofname)
            text_to_file_cp1251(shablon, ofname)
            info += ofname + '\n'
        except:
            pass
    
    #info += loger_pg('otmena')
    return info
