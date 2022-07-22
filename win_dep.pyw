from tkinter import *
import tkinter as tk
import tkinter
import tkinter.font as font
from tkinter import ttk
from typing import Any
from modules import *
import os
import sys
import subprocess
from papa_pg import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from win_dep_fun import *


class WinDep(WinDepFun):

    def __init__(self):
        self.root = Tk()

        self.bg_color = 'cyan'
        self.fg_color = 'blue'
        self.fg_color_contrast = 'darkblue'
        
        self.root["bg"] = "cyan"
        self.font_size = 20
        self.font_style = "Verdana"
        self.main_menu = Menu(self.root)
        self.root.config(menu=self.main_menu)
        self.bigfont = font.Font(family="Veranda",size=20)
        self.buttonFont = font.Font(size=20)

        self.STEP = 1
        self.PEREHOD = 15
        self.WIGHT_ENTRY = 24


    def menu_add(self, menu, data):
        for line in data:
            menu.add_command(label=line[0], command=line[1], font=(self.font_style, self.font_size))

    def mainmenu_add(self, data):
        for line in data:
            self.main_menu.add_cascade(label=line[0], menu=line[1])




    def win_dep_main(self):

        edit_menu_data = [
            ["find", self.edit_show],
            ["add", self.edit_add],
            ["delete", self.edit_delete],
                            ]      

        self.edit_menu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.edit_menu, edit_menu_data)


        navi_menu_data = [
            [" -->> ", self.edit_show],
            [" <<-- ", self.edit_add],
                            ]      

        self.navi_menu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.edit_menu, navi_menu_data)


        main_menu_data = [
            ["edit", self.edit_menu],
            ["navi", self.navi_menu],
        ]

        self.mainmenu_add(main_menu_data)

#__________________________________

        

        self.text_department = tk.StringVar()
        self.label_department = tk.Label(text='department', font='Verdana 20', bg='cyan' )\
            .grid(row=2, column=0, sticky=E)
        self.entry_department = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_department, foreground='blue', bg='lightcyan')\
            .grid(row=2, column=1, columnspan=1, sticky=E+W)

        self.text_region = tk.StringVar()
        self.label_region = tk.Label(text='region', font='Verdana 20', bg='cyan')\
            .grid(row=3, column=0, sticky=E)
        self.entry_region = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_region, bg='lightcyan')\
            .grid(row=3, column=1, columnspan=1, sticky=E+W)
            
        self.text_district_region = tk.StringVar()
        self.label_district_region = tk.Label(text='district_region', font='Verdana 20', bg='cyan')\
            .grid(row=4, column=0, sticky=E)
        self.entry_district_region = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_district_region, bg='lightcyan')\
            .grid(row=4, column=1, columnspan=1, sticky=E+W)

        self.text_district_city = tk.StringVar()
        self.label_district_city = tk.Label(text='district_city', font='Verdana 20', bg='cyan')\
            .grid(row=5, column=0, sticky=E)
        self.entry_district_city = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_district_city, bg='lightcyan')\
            .grid(row=5, column=1, columnspan=1, sticky=E+W) 

        self.text_city_type = tk.StringVar()
        self.label_city_type = tk.Label(text='city_type', font='Verdana 20', bg='cyan')\
            .grid(row=6, column=0, sticky=E)
        self.entry_city_type = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_city_type, bg='lightcyan')\
            .grid(row=6, column=1, columnspan=1, sticky=E+W) 

        self.text_city = tk.StringVar()
        self.label_city = tk.Label(text='city', font='Verdana 20', bg='cyan')\
            .grid(row=7, column=0, sticky=E)
        self.entry_city_type = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_city, bg='lightcyan')\
            .grid(row=7, column=1, columnspan=1, sticky=E+W) 

        self.text_street = tk.StringVar()
        self.label_street = tk.Label(text='street', font='Verdana 20', bg='cyan')\
            .grid(row=8, column=0, sticky=E)
        self.entry_street = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_street, bg='lightcyan')\
            .grid(row=8, column=1, columnspan=1, sticky=E+W) 

        self.text_street_type = tk.StringVar()
        self.label_street_type = tk.Label(text='street_type', font='Verdana 20', bg='cyan')\
            .grid(row=9, column=0, sticky=E)
        self.entry_street_type = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_street_type, bg='lightcyan')\
            .grid(row=9, column=1, columnspan=1, sticky=E+W) 

        self.text_hous = tk.StringVar()
        self.label_hous = tk.Label(text='hous', font='Verdana 20', bg='cyan')\
            .grid(row=10, column=0, sticky=E)
        self.entry_hous = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_hous, bg='lightcyan')\
            .grid(row=10, column=1, columnspan=1, sticky=E+W) 

        self.text_post_index = tk.StringVar()
        self.label_post_index = tk.Label(text='post_index', font='Verdana 20', bg='cyan')\
            .grid(row=11, column=0, sticky=E)
        self.entry_post_index = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_post_index, bg='lightcyan')\
            .grid(row=11, column=1, columnspan=1, sticky=E+W) 

        self.text_partner = tk.StringVar()
        self.label_partner = tk.Label(text='partner', font='Verdana 20', bg='cyan')\
            .grid(row=12, column=0, sticky=E)
        self.entry_partner = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_partner, bg='lightcyan')\
            .grid(row=12, column=1, columnspan=1, sticky=E+W) 

        self.text_status = tk.StringVar()
        self.label_status = tk.Label(text='status', font='Verdana 20', bg='cyan')\
            .grid(row=13, column=0, sticky=E)
        self.entry_status = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_status, bg='lightcyan')\
            .grid(row=13, column=1, columnspan=1, sticky=E+W) 

        self.text_register = tk.StringVar()
        self.label_register = tk.Label(text='register', font='Verdana 20', bg='cyan')\
            .grid(row=9, column=2, sticky=E)
        self.entry_register = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_register, bg='lightcyan')\
            .grid(row=9, column=3, columnspan=1, sticky=E+W) 

        self.text_edrpou = tk.StringVar()
        self.label_edrpou = tk.Label(text='edrpou', font='Verdana 20', bg='cyan')\
            .grid(row=10, column=2, sticky=E)
        self.entry_edrpou = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_edrpou, bg='lightcyan')\
            .grid(row=10, column=3, columnspan=1, sticky=E+W) 

        self.text_address = tk.StringVar()
        self.label_address = tk.Label(text='address', font='Verdana 20', bg='cyan')\
            .grid(row=16, column=0, sticky=E)
        self.entry_address = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_address, bg='lightcyan')\
            .grid(row=16, column=1, columnspan=5, sticky=E+W) 

        #______________________________________

        self.text_partner_name = tk.StringVar()
        self.label_partner_name = tk.Label(text='partner_name', font='Verdana 20', bg='cyan')\
            .grid(row=2, column=2, sticky=E)
        self.entry_partner_name = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_partner_name, bg='lightcyan')\
            .grid(row=2, column=3, columnspan=1, sticky=E+W) 

        self.text_id_terminal = tk.StringVar()
        self.label_id_terminal = tk.Label(text='id_terminal', font='Verdana 20', bg='cyan')\
            .grid(row=3, column=2, sticky=E)
        self.entry_id_terminal = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_id_terminal, bg='lightcyan')\
            .grid(row=3, column=3, columnspan=1, sticky=E+W) 

        self.text_koatu = tk.StringVar()
        self.label_koatu = tk.Label(text='koatu', font='Verdana 20', bg='cyan')\
            .grid(row=4, column=2, sticky=E)
        self.entry_koatu = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_koatu, bg='lightcyan')\
            .grid(row=4, column=3, columnspan=1, sticky=E+W) 

        self.text_tax_id = tk.StringVar()
        self.label_tax_id = tk.Label(text='tax_id', font='Verdana 20', bg='cyan')\
            .grid(row=5, column=2, sticky=E)
        self.entry_tax_id = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_tax_id, bg='lightcyan')\
            .grid(row=5, column=3, columnspan=1, sticky=E+W) 

        self.text_koatu2 = tk.StringVar()
        self.label_koatu2 = tk.Label(text='koatu2', font='Verdana 20', bg='cyan')\
            .grid(row=6, column=2, sticky=E)
        self.entry_koatu2 = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), textvariable=self.text_koatu2, bg='lightcyan')\
            .grid(row=6, column=3, columnspan=1, sticky=E+W) 

        #___________________________________________________

        #text_box = Text(font=(self.font_style, self.font_size), foreground='black', background='cyan')
        #text_box.grid(row=19, column=1, columnspan=3, rowspan=1)

        self.bigfont = font.Font(family="Verdana",size=20)
        self.root.option_add("*TCombobox*Listbox*Font", self.bigfont)

        self.text_info = tk.StringVar()
        self.entry_info = tk.Entry(width=self.WIGHT_ENTRY, font=(self.font_style, self.font_size), foreground='blue', textvariable=self.text_info, bg='lightblue')\
            .grid(row=18, column=1, columnspan=3, sticky=E+W) 

        self.label_combo_city_type = tk.Label(text='city_type', font='Verdana 20', bg='cyan')\
            .grid(row=11, column=3, columnspan=2, sticky=E)
        self.combo_city_type = ttk.Combobox(values=get_city_types())
        self.combo_city_type.grid(row=11, column=3)
        self.combo_city_type.current(0)
        self.combo_city_type.bind("<<ComboboxSelected>>", self.mk_combo_city_type)

        self.label_combo_streeet_type = tk.Label(text='street_type', font='Verdana 20', bg='cyan')\
            .grid(row=12, column=3, columnspan=2, sticky=E)
        self.combo_street_type = ttk.Combobox(values=get_street_types())
        self.combo_street_type.grid(row=12, column=3)
        self.combo_street_type.current(0)
        self.combo_street_type.bind("<<ComboboxSelected>>", self.mk_combo_street_type)

        self.label_combo_partner = tk.Label(text='partner', font='Verdana 20', bg='cyan')\
            .grid(row=13, column=3, columnspan=2, sticky=E)
        self.combo_partner = ttk.Combobox(values=['',] + get_partners())
        self.combo_partner.grid(row=13, column=3)
        self.combo_partner.current(0)
        self.combo_partner.bind("<<ComboboxSelected>>", self.mk_combo_partners)


#____________________________


        myFont = font.Font(size=24)

        self.button_find = tk.Button(text="найди", command=self.edit_show, bg='cyan', fg='blue')
        self.button_find.grid(row=1, column=0)
        self.button_find['font'] = self.buttonFont
        
        self.button_find['font'] = myFont

        self.button_find2 = tk.Button(text="найди", command=self.edit_show, bg='cyan', fg='blue')
        self.button_find2.grid(row=2, column=5, sticky=E+W)
        self.button_find2['font'] = self.buttonFont
        
        self.button_find2['font'] = myFont

        self.button_back = tk.Button(text="  <<  ", command=self.navi_backward, bg='cyan', fg='blue')
        self.button_back.grid(row=1, column=1)
        self.button_back['font'] = self.buttonFont
        
        self.button_back['font'] = myFont


        button_back2 = tk.Button(text="  <<  ", command=self.navi_backward, bg='cyan', fg='blue')
        button_back2.grid(row=3, column=5, sticky=E+W)
        button_back2['font'] = self.buttonFont
        
        button_back2['font'] = myFont

        button_forward = tk.Button(text="  >>  ", command=self.navi_forward, bg='cyan', fg='blue')
        button_forward.grid(row=1, column=2)
        button_forward['font'] = self.buttonFont
        
        button_forward['font'] = myFont


        button_forward2 = tk.Button(text="  >>  ", command=self.navi_forward, bg='cyan', fg='blue')
        button_forward2.grid(row=4, column=5, sticky=E+W)
        button_forward2['font'] = self.buttonFont
        
        button_forward2['font'] = myFont

        self.button_add = tk.Button(text="сохрани", command=self.edit_add, bg='cyan')
        self.button_add.grid(row=1, column=3)
        self.button_add['font'] = self.buttonFont
        
        self.button_add['font'] = myFont

        self.button_add2 = tk.Button(text="обнови", command=self.edit_update, bg='cyan')
        self.button_add2.grid(row=5, column=5, sticky=E+W)
        self.button_add2['font'] = self.buttonFont
        
        self.button_add2['font'] = myFont

        self.button_clear = tk.Button(text="очисти", command=self.clear_me, bg='cyan', fg='darkgreen')
        self.button_clear.grid(row=1, column=4)
        self.button_clear['font'] = self.buttonFont
        
        self.button_clear['font'] = myFont

        self.button_delete = tk.Button(text="удали", command=self.edit_delete, bg='cyan', fg='darkmagenta')
        self.button_delete.grid(row=10, column=5)
        self.button_delete['font'] = self.buttonFont
        
        self.button_delete['font'] = myFont

        self.button_mk_adr = tk.Button(text="адрес", command=self.mk_address, bg='cyan', fg='blue')
        self.button_mk_adr.grid(row=7, column=4, sticky=E+W)
        self.button_mk_adr['font'] = self.buttonFont
        
        self.button_mk_adr['font'] = myFont

        self.button_koatu2 = tk.Button(text="koatu2", command=self.win_dep_mk_koatu2, bg='cyan', fg='blue')
        self.button_koatu2.grid(row=8, column=4, sticky=E+W)
        self.button_koatu2['font'] = self.buttonFont
        
        self.button_mk_adr['font'] = myFont

        tk.Button(text="bottom", bg='cyan', fg='lightblue').grid(row=19, column=4)
        #tk.Button(text="fringle_1", bg='cyan').grid(row=18, column=4)
        #tk.Button(text="fringle_2", bg='cyan').grid(row=16, column=4)


        self.root.mainloop()


#data = []

w = WinDep()
w.win_dep_main()