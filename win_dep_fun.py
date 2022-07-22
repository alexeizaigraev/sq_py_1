from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from tkinter import *
#import tkinter
import tkinter as tk
import tkinter.font as font
from turtle import bgcolor, width
from typing import Any

import modules
import os
import sys
import subprocess
from papa_pg import *

class WinDepFun():

    def clear_combo(self):
        self.combo_city_type.current(0)
        self.combo_street_type.current(0)
        self.combo_partner.current(0)

    def clear_me(self):
        self.text_department.set('')
        self.text_region.set('')
        self.text_district_region.set('')
        self.text_district_city.set('')
        self.text_city_type.set('м.')
        self.text_city.set('')
        self.text_street.set('')
        self.text_street_type.set('вулиця')
        self.text_hous.set('')
        self.text_post_index.set('')
        self.text_partner.set('')
        self.text_status.set('')
        self.text_register.set('')
        self.text_edrpou.set('')
        self.text_address.set('')
        self.text_partner_name.set('')
        self.text_id_terminal.set('')
        self.text_koatu.set('')
        self.text_tax_id.set('')
        self.text_koatu2.set('')
        #text_info.set('')
        self.clear_combo()


    def get_windata(self):
        vec = [
            self.text_department.get(),
            self.text_region.get(),
            self.text_district_region.get(),
            self.text_district_city.get(),
            self.text_city_type.get(),
            self.text_city.get(),
            self.text_street.get(),
            self.text_street_type.get(),
            self.text_hous.get(),
            self.text_post_index.get(),
            self.text_partner.get(),
            self.text_status.get(),
            self.text_register.get(),
            self.text_edrpou.get(),
            self.text_address.get(),
            self.text_partner_name.get(),
            self.text_id_terminal.get(),
            self.text_koatu.get(),
            self.text_tax_id.get(),
            self.text_koatu2.get(),
        ]
        return vec

    def edit_show(self):
        key = str(self.text_department.get()).strip()
        if not key:
            return
        self.clear_me()
        data = get_one_dep_data(key)
        try:
            self.text_department.set(data[0])
            self.text_region.set(data[1])
            self.text_district_region.set(data[2]),
            self.text_district_city.set(data[3]),
            self.text_city_type.set(data[4]),
            self.text_city.set(data[5]),
            self.text_street.set(data[6]),
            self.text_street_type.set(data[7]),
            self.text_hous.set(data[8]),
            self.text_post_index.set(data[9]),
            self.text_partner.set(data[10]),
            self.text_status.set(data[11]),
            self.text_register.set(data[12]),
            self.text_edrpou.set(data[13]),
            self.text_address.set(data[14]),
            self.text_partner_name.set(data[15]),
            self.text_id_terminal.set(data[16]),
            self.text_koatu.set(data[17]),
            self.text_tax_id.set(data[18]),
            self.text_koatu2.set(data[19]),

            self.text_info.set(f'show {data[0]}')
        except:
            pass

    def navi_forward(self):
        key = str(self.text_department.get()).strip()
        if not key:
            return
        self.clear_me()
        data = get_one_dep_data(next_dep(key))
        try:
            self.text_department.set(data[0])
            self.text_region.set(data[1])
            self.text_district_region.set(data[2]),
            self.text_district_city.set(data[3]),
            self.text_city_type.set(data[4]),
            self.text_city.set(data[5]),
            self.text_street.set(data[6]),
            self.text_street_type.set(data[7]),
            self.text_hous.set(data[8]),
            self.text_post_index.set(data[9]),
            self.text_partner.set(data[10]),
            self.text_status.set(data[11]),
            self.text_register.set(data[12]),
            self.text_edrpou.set(data[13]),
            self.text_address.set(data[14]),
            self.text_partner_name.set(data[15]),
            self.text_id_terminal.set(data[16]),
            self.text_koatu.set(data[17]),
            self.text_tax_id.set(data[18]),
            self.text_koatu2.set(data[19]),

            self.text_info.set(f'show {data[0]}')
        except:
            pass

    def navi_backward(self):
        key = str(self.text_department.get()).strip()
        if not key:
            return
        self.clear_me()
        data = get_one_dep_data(pred_dep(key))
        try:
            self.text_department.set(data[0])
            self.text_region.set(data[1])
            self.text_district_region.set(data[2]),
            self.text_district_city.set(data[3]),
            self.text_city_type.set(data[4]),
            self.text_city.set(data[5]),
            self.text_street.set(data[6]),
            self.text_street_type.set(data[7]),
            self.text_hous.set(data[8]),
            self.text_post_index.set(data[9]),
            self.text_partner.set(data[10]),
            self.text_status.set(data[11]),
            self.text_register.set(data[12]),
            self.text_edrpou.set(data[13]),
            self.text_address.set(data[14]),
            self.text_partner_name.set(data[15]),
            self.text_id_terminal.set(data[16]),
            self.text_koatu.set(data[17]),
            self.text_tax_id.set(data[18]),
            self.text_koatu2.set(data[19]),

            self.text_info.set(f'show {data[0]}')
        except:
            pass

    def edit_add(self):
        data = self.get_windata()
        try:
            refresh_one_dep(data)
            self.text_info.set(f'+ {data[0]}')
        except Exception as ex:
            #clear_me()
            self.text_info.set(str(ex))

    def edit_update(self):
        data = self.get_windata()
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
            self.text_info.set(f'update {data[0]}')
        except Exception as ex:
            #clear_me()
            self.text_info.set(str(ex))

    

    def edit_delete(self):
        key = str(self.text_department.get()).strip()
        if not key:
            return
        try:
            del_dep(key)
            self.text_info.set(f'- {key}')
        except Exception as ex:
            self.text_info.set(str(ex) )
        

    def mk_combo_city_type(self, event):
        self.text_city_type.set(self.combo_city_type.get())
    def mk_combo_street_type(self, event):
        self.text_street_type.set(self.combo_street_type.get())
    def mk_combo_partners(self, event):
        self.text_partner.set(self.combo_partner.get())

    def mk_address(self):
        rez = ''
        post_index = self.text_post_index.get()
        if post_index:
            rez += post_index
        region = self.text_region.get()
        if region:
            rez += f' {region} обл.'
        district_region = self.text_district_region.get()
        if district_region:
            rez += f' {district_region} p-н.'
        city_type = self.text_city_type.get()
        if city_type:
            rez += f' {city_type}'
        city = self.text_city.get()
        if city:
            rez += f' {city}'
        district_city = self.text_district_city.get()
        if district_city:
            rez += f' {district_city} p-н.'
        street_type = self.text_street_type.get()
        if street_type:
            rez += f' {street_type}'
        street = self.text_street.get()
        if street:
            rez += f' {street}'
        hous = self.text_hous.get()
        if hous:
            rez += f' {hous}'
        self.text_address.set(rez)
        
    def win_dep_mk_koatu2(self):
        self.text_koatu2.set(mk_koatu2(self.text_city.get(), self.text_district_city.get(), self.text_koatu.get()))


    def enter_pressed(self, event):
        self.edit_add()

