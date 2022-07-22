from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from tkinter import *
#import tkinter
import tkinter as tk
import tkinter.font as font
from turtle import bgcolor, width
from typing import Any

#import modules
import os
import sys
import subprocess
from win_func import *
#from papa_pg import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

class Win(WinFunc):
    
    def __init__(self):
        self.bg_color = 'cyan'
        self.fg_color = 'blue'
        self.fg_color_contrast = 'darkblue'
        
        self.root = Tk()
        self.root["bg"] = "cyan"
        self.font_size = 18
        self.font_style = "Verdana"
        self.main_menu = Menu(self.root)
        self.root.config(menu=self.main_menu)
        self.bigfont = font.Font(family="Veranda",size=20)
        self.buttonFont = font.Font(size=20)

    def menu_add(self, menu, data):
        for line in data:
            menu.add_command(label=line[0], command=line[1], font=(self.font_style, self.font_size))
 
    def main_menu_add(self, data):
        for line in data:
            self.main_menu.add_cascade(label=line[0], menu=line[1])

    
    def mk_btn_fillX(self, vec):
            vec[0] = tk.Button(text=vec[1], command=vec[2], background = self.bg_color, foreground = self.fg_color_contrast)
            vec[0].pack(side='top', fill=X)
            vec[0]['font'] = self.buttonFont



    def win_main(self):

        lb_menu_data = [
            ["Терминалы", self.mk_terminals],
            ["Партнёры", self.mk_partners],
            ["Папки", self.mk_folders],
            ["Очисти", self.clear_lb]
                            ]      

        self.lb_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.lb_memu, lb_menu_data)


        people_menu_data = [
            ["Приём", self.people_priem],
            ["Отпуск", self.people_otpusk],
            ["Перевод", self.people_perevod],
            ["Рассылка", self.people_postall],
        ]

        self.people_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.people_memu, people_menu_data)



        some_menu_data = [
            ["Терминалы", self.some_term],
            ["Сайт", self.some_site],
            ["Кадры отбор", self.some_hr_otbor],
            ["Кадры", self.some_summury],
            ["Сводка АБ", self.some_hr_ab],
            ["Экв груп", self.some_ekv_group],
            ["Экв без обновл", self.some_ekv_lite],
            ["Наташа", self.some_natasha],
        ]
        
        self.some_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.some_memu, some_menu_data)
        

        otbor_menu_data = [
            ["Терминалы текст", self.otbor_term_text],
            ["Отделения текст", self.otbor_dep_text],
            ["ФН текст", self.otbor_fiscal_text],
            ["ЗН текст", self.otbor_serial_text],
            ["Все терминалы по отдениям", self.otbor_all_on_dep],

            ["Выбор", self.otbor_otbor],
            ["Отделения от до", self.otbor_text],
            ["Список отделений", self.otbor_text_list],
            ["Список терминалов", self.otbor_text_list_term],
            ["Список ЗН", self.otbor_text_list_serial],
            ["Хвосты ЗН", self.otbor_text_list_serial_hvost],
            ["ЗН из файла", self.otbor_serial_file],
            ["ФН из файла", self.otbor_fiscal_file],
            ["Покажи", self.show_otbor],
        ]

        self.otbor_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.otbor_memu, otbor_menu_data)


        monitor_memu_data = [
            ["Расклад", self.monitor_rasklad],
            ["Бекап", self.monitor_accback],
            ["Монитор", self.monitor_monitor],
            ["РП отбор", self.monitor_get_rp],
            ["РП партнёр", self.monitor_get_rp_all],
            ["Жнец копи", self.monitor_gnetz_copy],
            ["Жнец муви", self.monitor_gnetz_move],
            ["Гугл бекап общий", self.monitor_gdrive_backup_comon],
            ["Гугл бекап дата", self.monitor_gdrive_backup_date],
        ]


        self.monitor_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.monitor_memu, monitor_memu_data)
        
        
        kabinet_menu_data = [
            ["Рро", self.kabinet_rro],
            ["Переезд", self.kabinet_pereezd],
            ["Отмена", self.kabinet_otmena],
            ["Прро", self.kabinet_prro],
            ["Книги", self.kabinet_knigi],
        ]

        self.kabinet_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.kabinet_memu, kabinet_menu_data)


        clear_memu_data = [
            ["Очистка", self.clear_me],
        ]

        self.clear_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.clear_memu, clear_memu_data)
        
        
        actual_menu_data = [
            ["Удали отделения отбор", self.actual_del_otbor_dep],
            ["Удали терминалы отбор", self.actual_del_otbor_term],
        ]

        self.actual_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.actual_memu, actual_menu_data)

        
        doc_menu_data = [
            ["Бекап", self.doc_pg_back],
            ["Активация", self.doc_activaciya],
            ["Дективация", self.doc_deactivaciya],
            ["Акт передачи", self.doc_act_peredachi],
            ["Распломбирование", self.doc_rasplomb],
            ["Отделения", self.doc_dep],
            ["Терминалы", self.doc_term],
            ["Логи", self.doc_logi],
        ]


        self.doc_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.doc_memu, doc_menu_data)
        

        refresh_memu_data = [
            ["indata -> pg", self.refresh_from_indata],
            ["gdrive -> pg", self.gdrive_to_pg],
            
            ["ekv", self.refresh_ekv],
            
            ["pg -> access", self.refresh_to_access],
            
            ["pg -> gdrive", self.monitor_accback],
        ]

        self.refresh_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.refresh_memu, refresh_memu_data)
        
        
        edit_menu_data = [
            [" + Отделения из файла", self.edit_dep_from_file],
            [" + Терминалы из файла", self.edit_term_from_file],
            ["Удали отделения отбор", self.actual_del_otbor_dep],
            ["Удали терминалы отбор", self.actual_del_otbor_term],
        ]

        self.edit_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.edit_memu, edit_menu_data)
        
        
        win_menu_data = [
            ["Отделения", self.win_dep],
            ["Терминалы", self.win_term],
            ["Кабинет", self.win_kabinet],
            ["Окно", self.win_win],
        ]

        self.win_memu = Menu(self.main_menu, tearoff=0, bg = 'cyan', fg='darkblue')
        self.menu_add(self.win_memu, win_menu_data)
        
        

        main_menu_data = [
            ["Люди", self.people_memu],
            ["Всячина", self.some_memu],
            ["Монитор", self.monitor_memu],
            ["Кабинет", self.kabinet_memu],

            ["Очистка", self.clear_memu],
            ["Актуаль", self.actual_memu],
            ["Доки", self.doc_memu],

            ["Отбор", self.otbor_memu],
            ["Обнови", self.refresh_memu],
            ["Окна", self.win_memu],
            ["Добавь", self.edit_memu],
            ["Листбокс", self.lb_memu],
        ]

        self.main_menu_add(main_menu_data)



        self.text_box = Text(font=(self.font_style, self.font_size), width=70, foreground='darkmagenta', background='cyan')
        self.text_box.pack(side='left', padx=10, pady=10)
        self.scroll_text = Scrollbar(command=self.text_box.yview)
        self.scroll_text.pack(side='left', fill=Y)
        self.text_box.config(yscrollcommand=self.scroll_text.set)


        self.lb = Listbox(selectmode=EXTENDED, font=(self.font_style, self.font_size), foreground = self.fg_color, background='cyan', width=10)
        self.lb.pack(side='left', fill=Y, padx=10, pady=10)
        self.scroll_terminals = Scrollbar(command=self.lb.yview)
        self.scroll_terminals.pack(side='left', fill=Y)
        self.lb.config(yscrollcommand=self.scroll_terminals.set)


        self.buttonFont = font.Font(size=18)

        self.button_clear = None
        self.mk_btn_fillX([self.button_clear, "очисти", self.clear_me])

        self.button_input = None
        self.mk_btn_fillX([self.button_input, "из текста", self.otbor_text])

        self.btn = None
        self.mk_btn_fillX([self.btn, "из списка", self.otbor_otbor])

        self.btn_term = None
        self.mk_btn_fillX([self.btn_term, "терминалы", self.mk_terminals])

        self.btn_partn = None
        self.mk_btn_fillX([self.btn_partn, "партнёры", self.mk_partners])

        self.btn_term_partn = None
        self.mk_btn_fillX([self.btn_term_partn, "терм партн", self.mk_term_partn])

        self.button_summury_partn = None
        self.mk_btn_fillX([self.button_summury_partn, "кадры партн", self.some_summury])

        self.btn_fold = None
        self.mk_btn_fillX([self.btn_fold, "папки", self.mk_folders])

        self.btn_clearlb = None
        self.mk_btn_fillX([self.btn_clearlb, "сотри лб", self.clear_lb])


        self.button_refresh_from_gdrive = tk.Button(text="gdrive -> pq", command=self.gdrive_to_pg, background = self.bg_color, foreground='darkgreen')
        self.button_refresh_from_gdrive.pack(side='top', padx=10, pady=10, fill=X)
        self.button_refresh_from_gdrive['font'] = self.buttonFont



        self.button_refresh_from_indata = tk.Button(text="in_data -> pq", command=self.refresh_from_indata, background = self.bg_color, foreground='darkgreen')
        self.button_refresh_from_indata.pack(side='top', padx=10, pady=10, fill=X)
        self.button_refresh_from_indata['font'] = self.buttonFont


        self.btn_windep = tk.Button(text="отделения", command=self.win_dep, background = self.bg_color, foreground = self.fg_color)
        self.btn_windep.pack(side='top', fill=X)
        self.btn_windep['font'] = self.buttonFont

        self.btn_winterm = tk.Button(text="терминалы", command=self.win_term, background = self.bg_color, foreground = self.fg_color)
        self.btn_winterm.pack(side='top', fill=X)
        self.btn_winterm['font'] = self.buttonFont

        self.btn_winkabinet = tk.Button(text="кабинет", command=self.win_kabinet, background = self.bg_color, foreground = self.fg_color)
        self.btn_winkabinet.pack(side='top', fill=X)
        self.btn_winkabinet['font'] = self.buttonFont


        self.button_refresh_to_indata = tk.Button(text="pg -> in_data", command=self.pg_to_indata, background = self.bg_color, foreground='darkmagenta')
        self.button_refresh_to_indata.pack(side='top', padx=10, pady=10, fill=X)
        self.button_refresh_to_indata['font'] = self.buttonFont


        try:
            self.partners = get_partners()
        except:
            pass
        try:
            self.folders = get_list('SELECT gdrive FROM comon_data;')
        except:
            pass
        try:
            self.terminals = get_terminals_list()
        except:
            pass
        self.lb_status = 'term'

        

        self.root.geometry("1600x800")
        self.root.mainloop()
        

w = Win()
w.win_main()
