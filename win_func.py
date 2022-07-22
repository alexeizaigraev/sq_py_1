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


class WinFunc:

    def clear_me(self):
        self.text_box.delete(1.0, END)


    def work(self, ff):
        self.clear_me()
        try:
            u = ff()
            self.text_box.insert(1.0, u)
        except Exception as ex:
            self.text_box.insert(1.0, str(ex))

    def work_param(self, ff, param):
        self.clear_me()
        try:
            u = ff(param)
            self.text_box.insert(1.0, u)
        except Exception as ex:
            self.text_box.insert(1.0, str(ex))


    def refresh_to_access(self):
        self.clear_me()
        txt = ''
    
        txt += select_deps_to_indata()
        txt += select_terms_to_indata()
        
        app_path = 'C:/ToAccessRelease/ToAccess1.exe'
        try:
            os.system(app_path)
            #clear_me()
            txt += 'ToAccess1 finish\n'
        except Exception as ex:
            txt += f'{str(ex)}\n\n'
        self.text_box.insert(1.0, txt)


    def refresh_from_indata(self):
        from refresh.refresh_from_indata import main
        u = main
        self.work(u)

    def refresh_ekv(self):
        from refresh.refresh_ekv import main
        u = main
        self.work(u)



    def people_priem(self):
        from people.priem import Priem
        self.clear_me()
        try:
            u = Priem()
            u.priem_main()
            self.text_box.insert(1.0, u.info)
        except Exception as ex:
            self.text_box.insert(1.0, str(ex))
    
    def people_otpusk(self):
        from people.otpusk import Otpusk
        self.clear_me()
        try:
            u = Otpusk()
            u.otpusk_main()
            self.text_box.insert(1.0, u.info)
        except Exception as ex:
            self.text_box.insert(1.0, str(ex))
    
    def people_perevod(self):
        from people.perevod import Perevod
        self.clear_me()
        try:
            u = Perevod()
            u.perevod_main()
            self.text_box.insert(1.0, u.info)
        except Exception as ex:
            self.text_box.insert(1.0, str(ex))

    def people_postall(self):
        from people.postall import Postall
        self.clear_me()
        try:
            u = Postall()
            u.postall_main()
            self.text_box.insert(1.0, u.info)
        except Exception as ex:
            self.text_box.insert(1.0, str(ex))



    def some_term(self):
        from some.pg_term import Term
        text = ''
        self.clear_me()
        try:
            u = Term()
            u.main_term()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def some_site(self):
        from some.site import main
        u = main
        self.work(u)

    def some_hr_otbor(self):
        from some.hr_otbor import main
        u = main
        self.work(u)

    def some_summury(self):
        from some.pg_summury import Summury
        self.clear_me()
        selected_items  = self.lb.curselection()
        partner_choise = self.partners[selected_items[0]]
        text = ''
        try:
            get_terminals_list_partner(partner_choise)
            u = Summury(partner_choise)
            u.main_summury()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def some_hr_ab(self):
        from some.hr_ab import main
        u = main
        self.work(u)

    def some_ekv_group(self):
        from some.ekv_group import main
        u = main
        self.work(u)

    def some_ekv_lite(self):
        from some.ekv_lite import main
        u = main
        self.work(u)


    def some_natasha(self):
        from some.natasha import main
        u = main
        self.work(u)

  
    def otbor_text(self):
        from otbor.add_otbor import Otbor
        mytext = str(self.text_box.get(1.0, END)).strip()
        text = ''
        
        try:
            u = Otbor(mytext)
            u.otbor_main()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.clear_me()    
        self.text_box.insert(1.0, text)
        
    def otbor_text_list(self):
        from otbor.add_otbor_hard_dep import OtborHardDep
        mytext = str(self.text_box.get(1.0, END)).strip()
        text = ''
        
        try:
            u = OtborHardDep(mytext)
            u.main_otbor_hard_dep()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.clear_me()
        self.text_box.insert(1.0, text)

    def otbor_term_text(self):
        from otbor.otbor_term_text import main
        mytext = str(self.text_box.get(1.0, END)).strip()
        self.work_param(main, mytext)

    def otbor_dep_text(self):
        from otbor.otbor_dep_text import main
        mytext = str(self.text_box.get(1.0, END)).strip()
        self.work_param(main, mytext)

    def otbor_fiscal_text(self):
        from otbor.otbor_fiscal_text import main
        mytext = str(self.text_box.get(1.0, END)).strip()
        self.work_param(main, mytext)

    def otbor_serial_text(self):
        from otbor.otbor_serial_text import main
        mytext = str(self.text_box.get(1.0, END)).strip()
        self.work_param(main, mytext)

    def otbor_all_on_dep(self):
        from otbor.otbor_all_on_dep import main
        mytext = str(self.text_box.get(1.0, END)).strip()
        self.work_param(main, mytext)

    def otbor_text_list_term(self):
        from otbor.add_otbor_hard_term import OtborHardTerm
        mytext = str(self.text_box.get(1.0, END)).strip()
        text = ''
        
        try:
            u = OtborHardTerm(mytext)
            u.main_otbor_hard_term()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.clear_me()
        self.text_box.insert(1.0, text)




    def otbor_text_list_serial(self):
        from otbor.add_otbor_serial import OtborSerial
        mytext = str(self.text_box.get(1.0, END)).strip()
        text = ''
        
        try:
            u = OtborSerial(mytext)
            u.main_otbor_serial()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.clear_me()    
        self.text_box.insert(1.0, text)


    def otbor_text_list_serial_hvost(self):
        from otbor.add_otbor_serial_hvost import OtborSerialHvost
        mytext = str(self.text_box.get(1.0, END)).strip()
        text = ''
        
        try:
            u = OtborSerialHvost(mytext)
            u.main_otbor_serial_hvost()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.clear_me()    
        self.text_box.insert(1.0, text)

    def otbor_serial_file(self):
        from otbor.add_otbor_serial_file import OtborSerialFile
        text = ''
        try:
            u = OtborSerialFile()
            u.main_otbor_serial_file()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.clear_me()
        self.text_box.insert(1.0, text)

    def otbor_fiscal_file(self):
        from otbor.otbor_fiscal_file import main
        u = main
        self.work(u)
        
    def otbor_otbor(self):
        from otbor.add_otbor_hard import OtborHard
        if self.lb_status == 'term':
            self.clear_me()
            values = [self.lb.get(idx) for idx in self.lb.curselection()]
            try:
                u = OtborHard(values)
                u.main_otbor_hard()
                self.text_box.insert(1.0, u.info)
            except Exception as ex:
                self.text_box.insert(1.0, str(ex))
        elif self.lb_status == 'partn':
            partner_choise  = self.partners[self.lb.curselection()[0]]
            if partner_choise:
                terminals = get_terminals_list_partner(partner_choise)
                self.clear_lb()
                for item in terminals:
                    self.lb.insert(END, item)
                self.lb_status = 'term'
        else:
            self.clear_me()
            self.text_box.insert(1.0, '\nДа ладно :)')



    def monitor_rasklad(self):
        from monitor.walker import Walker
        self.clear_me()
        try:
            u = Walker()
            u.walker_main()
            self.text_box.insert(1.0, u.info)
        except Exception as ex:
            self.text_box.insert(1.0, str(ex))

    def monitor_accback(self):
        from monitor.accback import accback
        u = accback
        self.work(u)
        
    def monitor_monitor(self):
        from monitor.monitor import main
        u = main
        self.work(u)

    def monitor_get_rp(self):
        from monitor.get_rp import get_rp
        u = get_rp
        self.work(u)
        
    def monitor_get_rp_all(self):
        from monitor.get_rp_all import GetRpAll
        self.clear_me()
        selected_items  = self.lb.curselection()
        choise = self.folders[selected_items[0]]
        text = ''
        try:
            u = GetRpAll(choise)
            u.get_rp_all_main()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
            #text = '123'
        self.text_box.insert(1.0, text)
    
    def monitor_gnetz_copy(self):
        from monitor.gnetz import Gnetz
        kind = 'copy'
        text = ''
        self.clear_me()
        try:
            u = Gnetz(kind)
            u.gnetz_main()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def monitor_gnetz_move(self):
        from monitor.gnetz import Gnetz
        kind = 'move'
        text = ''
        self.clear_me()
        try:
            u = Gnetz(kind)
            u.gnetz_main()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)  

    def monitor_gdrive_backup_comon(self):
        from monitor.gdrive_backup_comon import GdriveBackComon
        text = ''
        self.clear_me()
        try:
            u = GdriveBackComon()
            u.gdriveback_comon_main()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)  

    def monitor_gdrive_backup_date(self):
        from monitor.gdrive_backup_date import GdriveBackDate
        kind = 'move'
        text = ''
        self.clear_me()
        try:
            u = GdriveBackDate()
            u.gdrive_back_date_main()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)



    def kabinet_rro(self):
        from kabinet.rro import main
        u = main
        self.work(u)

    def kabinet_pereezd(self):
        from kabinet.pereezd import main
        u = main
        self.work(u)

    def kabinet_otmena(self):
        from kabinet.otmena import main
        u = main
        self.work(u)
        
    def kabinet_prro(self):
        from kabinet.prro import main
        u = main
        self.work(u)
        
    def kabinet_knigi(self):
        from kabinet.knigi import main
        u = main
        self.work(u)


    def actual_del_otbor_dep(self):
        from db.del_otbor_dep import DelOtborDep
        text = ''
        self.clear_me()
        try:
            u = DelOtborDep()
            u.main_del_otbor_dep()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def actual_del_otbor_term(self):
        #from db.del_otbor_term import DelOtborTerm
        info = ''
        q = 'SELECT * FROM OTBOR'
        otbor = get_data(q)
        for line in otbor:
            term = line[0]
            try:
                del_term(term)
                info += f'- {term}\n'
            except Exception as ex:
                info += f'{ex}\n'
        self.text_box.insert(1.0, info)


    def doc_activaciya(self):
        from doc.activaciya import Activaciya
        text = ''
        self.clear_me()
        try:
            u = Activaciya()
            u.main_activaciya()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)
        

    
    def doc_deactivaciya(self):
        from doc.deactivaciya import DeActivaciya
        text = ''
        self.clear_me()
        try:
            u = DeActivaciya()
            u.main_deactivaciya()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def doc_act_peredachi(self):
        from doc.act_peredachi import ActPeredachi
        text = ''
        self.clear_me()
        try:
            u = ActPeredachi()
            u.main_act_peredachi()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)


    def doc_rasplomb(self):
        from doc.rasplomb import Rasplomb
        text = ''
        self.clear_me()
        try:
            u = Rasplomb()
            u.main()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)



    def doc_dep(self):
        from doc.dep_to_file import DepToFile
        text = ''
        self.clear_me()
        try:
            u = DepToFile()
            u.main_dep_to_file()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def doc_term(self):
        from doc.term_to_file import TermToFile
        text = ''
        self.clear_me()
        try:
            u = TermToFile()
            u.main_term_to_file()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def doc_logi(self):
        from doc.logi_to_file import LogiToFile
        text = ''
        self.clear_me()
        try:
            u = LogiToFile()
            u.main_logi_to_file()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def doc_pg_back(self):
        from doc.doc_pg_back import DocPgBack
        text = ''
        self.clear_me()
        try:
            u = DocPgBack()
            u.main_doc_pg_back()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)



    def edit_dep_from_file(self):
        from edit.dep_from_file import DepFromFile
        text = ''
        self.clear_me()
        try:
            u = DepFromFile()
            u.main_dep_from_file()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)

    def edit_term_from_file(self):
        from edit.term_from_file import TermFromFile
        text = ''
        self.clear_me()
        try:
            u = TermFromFile()
            u.main_term_from_file()
            text += u.info + '\n'
        except Exception as ex:
            text += str(ex) + '\n'
        self.text_box.insert(1.0, text)




    def clear_lb(self):
        #terms = get_terminals_list()
        self.lb.delete(0, END)


    def mk_partners(self):
        self.clear_lb()
        partners = get_partners()
        for partner in partners:
            self.lb.insert(END, partner)
        self.lb_status = 'partn'


    def mk_terminals(self):
        self.clear_lb()
        terminals = get_terminals_list()
        for terminal in terminals:
            self.lb.insert(END, terminal)
        self.lb_status = 'term'

    def mk_folders(self):
        self.clear_lb()
        q = """SELECT gdrive
        FROM comon_data;"""
        items = get_list(q)
        for item in items:
            self.lb.insert(END, item)
        self.lb_status = 'fold'
    


    """
    if self.lb_status[0] == 'partn':
            partner_choise  = partners[lb.curselection()[0]]
            if partner_choise:
                clear_lb()
                terminals = get_terminals_list_partner(partner_choise)
                for item in terminals:
                    lb.insert(END, item)
                self.lb_status[0] = 'term'
                """

    def refresh_lb(self):
        if self.lb_status == 'term':
            self.otbor_otbor()
        elif self.lb_status == 'partn':
            self.mk_partners()
        elif self.lb_status == 'fold':
            self.mk_folders()
        else:
            self.mk_terminals()

    def mk_term_partn(self):
        partner_choise  = self.partners[self.lb.curselection()[0]]
        if partner_choise:
            terminals = get_terminals_list_partner(partner_choise)
            self.clear_lb()
            for item in terminals:
                self.lb.insert(END, item)
            self.lb_status = 'term'

    def pg_to_indata(self):
        self.clear_me()
        txt = ''
        txt += select_deps_to_file()
        txt += select_terms_to_file()
        """
        app_path = 'C:/ToAccessRelease/ToAccess1.exe'
        try:
            os.system(app_path)
            #clear_me()
            txt += 'ToAccess1 finish\n'
        except Exception as ex:
            txt += f'{str(ex)}\n\n'
        """
        self.text_box.insert(1.0, txt)


    def gdrive_to_pg(self):
        from refresh.rungdrive import main
        u = main
        self.work(u)
          
    

    def win_dep(self):
        os.system(f'{PYTHON_NAME} win_dep.pyw')
    def win_term(self):
        os.system(f'{PYTHON_NAME} win_term.pyw')
    def win_kabinet(self):
        os.system(f'{PYTHON_NAME} win_kabinet.pyw')
    def win_win(self):
        os.system(f'{PYTHON_NAME} win.pyw')

    def show_otbor(self):
        self.clear_me()
        q = 'SELECT * FROM otbor'
        data = get_data(q)
        txt = str(data).replace("[('", '').replace("')]", '').replace('), (', '\n').replace("'", '')
        self.text_box.insert(1.0, str(txt))

    def enter_pressed(self, event):
        txt = str(text_box.get(1.0, END)).strip()
        #clear_me()
        if ' ' not in txt:
            if len(txt) == 7:
                self.otbor_text()
            else:
                self.otbor_text_list_term()
        else:
            split_text = txt.split(' ')
            if len(split_text[0]) == 7:
                if len(split_text) == 2:
                    self.otbor_text()
                else:
                    self.otbor_text_list()
            else:
                self.otbor_text_list_term()
