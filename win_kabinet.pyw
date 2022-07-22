from tkinter import *
import tkinter as tk
#import tkinter
import tkinter.font as font
from tkinter import ttk
from typing import Any
from modules import *
import os
import sys
import subprocess
from papa_pg import *

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def clear_combo():
    combo_owner.current(0)
    combo_model.current(0)
    combo_soft.current(0)

def clear_me():
    text_department.set('')
    text_termial.set('')
    text_model.set('')
    text_serial_number.set('')
    text_date_manufacture.set('')
    text_soft.set('4.00 UA')
    text_producer.set('ДАТЕКС ООД')
    text_rne_rro.set('')
    text_sealing.set('')
    text_fiscal_number.set('')
    text_oro_serial.set('')
    text_oro_number.set('1')
    text_ticket_serial.set('')
    text_ticket_1sheet.set('')
    text_ticket_number.set('1')
    text_sending.set('')
    text_books_arhiv.set('')
    text_tickets_arhiv.set('')
    text_to_rro.set('ТОВ ПОС')

    text_owner_rro.set('')
    text_register.set('')
    text_finish.set('')

    text_address.set('')
    text_koatu.set('')
    text_tax_id.set('')
    text_koatu2.set('')

    clear_combo()



def get_windata():
    vec = [
        text_department.get(),
        text_termial.get(),
        text_model.get(),
        text_serial_number.get(),
        text_date_manufacture.get(),
        text_soft.get(),
        text_producer.get(),
        text_rne_rro.get(),
        text_sealing.get(),
        text_fiscal_number.get(),
        text_oro_serial.get(),
        text_oro_number.get(),
        text_ticket_serial.get(),
        text_ticket_1sheet.get(),
        text_ticket_number.get(),
        text_sending.get(),
        text_books_arhiv.get(),
        text_tickets_arhiv.get(),
        text_to_rro.get(),
        text_owner_rro.get(),
        text_register.get(),
        text_finish.get(),
    ]
    if vec[0] == '':
        vec[0] = vec[1][:7]
    return vec

def edit_show():
    key = str(text_termial.get()).strip()
    if not key:
        return
    clear_me()
    data = get_one_term_data(key)[0]
    try:
        text_department.set(data[0])
        text_termial.set(data[1])
        text_model.set(data[2]),
        text_serial_number.set(data[3]),
        text_date_manufacture.set(data[4]),
        text_soft.set(data[5]),
        text_producer.set(data[6]),
        text_rne_rro.set(data[7]),
        text_sealing.set(data[8]),
        text_fiscal_number.set(data[9]),
        text_oro_serial.set(data[10]),
        text_oro_number.set(data[11]),
        text_ticket_serial.set(data[12]),
        text_ticket_1sheet.set(data[13]),
        text_ticket_number.set(data[14]),
        text_sending.set(data[15]),
        text_books_arhiv.set(data[16]),
        text_tickets_arhiv.set(data[17]),
        text_to_rro.set(data[18]),
        text_owner_rro.set(data[19]),
        text_register.set(data[20]),
        text_finish.set(data[21]),

        try:
            text_address.set(get_address(data[0]))
        except:
            pass
        try:
            text_koatu.set(get_koatu(data[0]))
        except:
            pass
        try:
            text_tax_id.set(get_tax_id(data[0]))
        except:
            pass
        try:
            text_koatu2.set(get_koatu2(data[0]))
        except:
            pass

        text_info.set(f'show {data[1]}')
    except:
        pass

def navi_forward():
    key = str(text_termial.get()).strip()
    if not key:
        return
    clear_me()
    data = get_one_term_data(next_term(key))[0]
    try:
        text_department.set(data[0])
        text_termial.set(data[1])
        text_model.set(data[2]),
        text_serial_number.set(data[3]),
        text_date_manufacture.set(data[4]),
        text_soft.set(data[5]),
        text_producer.set(data[6]),
        text_rne_rro.set(data[7]),
        text_sealing.set(data[8]),
        text_fiscal_number.set(data[9]),
        text_oro_serial.set(data[10]),
        text_oro_number.set(data[11]),
        text_ticket_serial.set(data[12]),
        text_ticket_1sheet.set(data[13]),
        text_ticket_number.set(data[14]),
        text_sending.set(data[15]),
        text_books_arhiv.set(data[16]),
        text_tickets_arhiv.set(data[17]),
        text_to_rro.set(data[18]),
        text_owner_rro.set(data[19]),
        text_register.set(data[20]),
        text_finish.set(data[21]),

        try:
            text_address.set(get_address(data[0]))
        except:
            pass
        try:
            text_koatu.set(get_koatu(data[0]))
        except:
            pass
        try:
            text_tax_id.set(get_tax_id(data[0]))
        except:
            pass
        try:
            text_koatu2.set(get_koatu2(data[0]))
        except:
            pass

        text_info.set(f'show {data[1]}')
    except:
        pass

def navi_backward():
    key = str(text_termial.get()).strip()
    if not key:
        return
    clear_me()
    data = get_one_term_data(pred_term(key))[0]
    try:
        text_department.set(data[0])
        text_termial.set(data[1])
        text_model.set(data[2]),
        text_serial_number.set(data[3]),
        text_date_manufacture.set(data[4]),
        text_soft.set(data[5]),
        text_producer.set(data[6]),
        text_rne_rro.set(data[7]),
        text_sealing.set(data[8]),
        text_fiscal_number.set(data[9]),
        text_oro_serial.set(data[10]),
        text_oro_number.set(data[11]),
        text_ticket_serial.set(data[12]),
        text_ticket_1sheet.set(data[13]),
        text_ticket_number.set(data[14]),
        text_sending.set(data[15]),
        text_books_arhiv.set(data[16]),
        text_tickets_arhiv.set(data[17]),
        text_to_rro.set(data[18]),
        text_owner_rro.set(data[19]),
        text_register.set(data[20]),
        text_finish.set(data[21]),

        try:
            text_address.set(get_address(data[0]))
        except:
            pass
        try:
            text_koatu.set(get_koatu(data[0]))
        except:
            pass
        try:
            text_tax_id.set(get_tax_id(data[0]))
        except:
            pass
        try:
            text_koatu2.set(get_koatu2(data[0]))
        except:
            pass

        text_info.set(f'show {data[1]}')
    except:
        pass

def edit_add():
    data = get_windata()
    try:
        refresh_one_term(data)
        text_info.set(f'+ {data[1]}')
    except Exception as ex:
        #clear_me()
        text_info.set(str(ex))

def edit_delete():
    key = str(text_termial.get()).strip()
    if not key:
        return
    try:
        del_term(key)
        text_info.set(f'- {key}')
    except Exception as ex:
        text_info.set(str(ex) )

def mk_combo_owners(event):
    text_owner_rro.set(combo_owner.get())

def mk_combo_models(event):
    text_model.set(combo_model.get())

def mk_combo_softs(event):
    text_soft.set(combo_soft.get())

def mk_dep():
    text_department.set(text_termial.get()[:7])
    

root = Tk()

data = []


font_size = 18
font_style = "Verdana"

main_menu = Menu(root)

edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="show", command=edit_show, font=(font_style, font_size))
edit_menu.add_command(label="add", command=edit_add, font=(font_style, font_size))
edit_menu.add_command(label="delete", command=edit_delete, font=(font_style, font_size))

navi_menu = Menu(main_menu, tearoff=0)
navi_menu.add_command(label=" -->> ", command=navi_forward, font=(font_style, font_size))
navi_menu.add_command(label=" <<-- ", command=navi_backward, font=(font_style, font_size))

main_menu.add_cascade(label="edit",
                     menu=edit_menu)
main_menu.add_cascade(label="navi",
                     menu=navi_menu)

buttonFont = font.Font(size=18)


button_find = tk.Button(text="найди", command=edit_show)
button_find.grid(row=1, column=0)
button_find['font'] = buttonFont

button_find2 = tk.Button(text="найди", command=edit_show) 
button_find2.grid(row=3, column=5, sticky=E+W)
button_find2['font'] = buttonFont

button_back = tk.Button(text="  <<  ", command=navi_backward)
button_back.grid(row=1, column=1)
button_back['font'] = buttonFont

button_back2 = tk.Button(text="  <<  ", command=navi_backward)
button_back2.grid(row=4, column=5, sticky=E+W)
button_back2['font'] = buttonFont

button_forward = tk.Button(text="  >>  ", command=navi_forward)
button_forward.grid(row=1, column=2)
button_forward['font'] = buttonFont

button_forward2 = tk.Button(text="  >>  ", command=navi_forward)
button_forward2.grid(row=5, column=5, sticky=E+W)
button_forward2['font'] = buttonFont

button_add = tk.Button(text="сохрани", command=edit_add, bg='lightcyan')
button_add.grid(row=1, column=3)
button_add['font'] = buttonFont

button_add2 = tk.Button(text="сохрани", command=edit_add, bg='lightcyan')
button_add2.grid(row=6, column=5, sticky=E+W)
button_add2['font'] = buttonFont

button_clear = tk.Button(text="очисти", command=clear_me, bg='lightgreen', )
button_clear.grid(row=1, column=4, sticky=E+W)
button_clear['font'] = buttonFont

button_delete = tk.Button(text="удали", command=edit_delete, fg='white', bg='blue')
button_delete.grid(row=9, column=5)
button_delete['font'] = buttonFont

tk.Button(text="bottom", bg='cyan').grid(row=22, column=4)
tk.Button(text="fringl_1", bg='cyan').grid(row=18, column=4)
tk.Button(text="fringl_2", bg='cyan').grid(row=21, column=4)

button_mk_dep = tk.Button(text="отделение", command=mk_dep)
button_mk_dep.grid(row=7, column=4, sticky=E+W)
button_mk_dep['font'] = buttonFont

STEP = 1
PEREHOD = 15
WIGHT_ENTRY = 33


text_termial = tk.StringVar()
label_termial = tk.Label(text='term', font='Verdana 18', bg='cyan')\
    .grid(row=3, column=0, sticky=E)
entry_termial = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_termial, foreground='blue')\
    .grid(row=3, column=1, columnspan=1, sticky=E+W)

text_department = tk.StringVar()
label_department = tk.Label(text='dep', font='Verdana 18', bg='cyan' )\
    .grid(row=4, column=0, sticky=E)
entry_department = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_department)\
    .grid(row=4, column=1, columnspan=1, sticky=E+W)
    
text_model = tk.StringVar()
label_model = tk.Label(text='model', font='Verdana 18', bg='cyan')\
    .grid(row=5, column=0, sticky=E)
entry_model = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_model)\
    .grid(row=5, column=1, columnspan=1, sticky=E+W)

text_serial_number = tk.StringVar()
label_serial_number = tk.Label(text='serial', font='Verdana 18', bg='cyan')\
    .grid(row=6, column=0, sticky=E)
entry_serial_number = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_serial_number)\
    .grid(row=6, column=1, columnspan=1, sticky=E+W) 

text_date_manufacture = tk.StringVar()
label_date_manufacture = tk.Label(text='manuf', font='Verdana 18', bg='cyan')\
    .grid(row=7, column=0, sticky=E)
entry_date_manufacture = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_date_manufacture)\
    .grid(row=7, column=1, columnspan=1, sticky=E+W) 

text_soft = tk.StringVar()
label_soft = tk.Label(text='soft', font='Verdana 18', bg='cyan')\
    .grid(row=8, column=0, sticky=E)
entry_soft = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_soft)\
    .grid(row=8, column=1, columnspan=1, sticky=E+W) 

text_producer = tk.StringVar()
label_producer = tk.Label(text='producer', font='Verdana 18', bg='cyan')\
    .grid(row=9, column=0, sticky=E)
entry_producer = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_producer)\
    .grid(row=9, column=1, columnspan=1, sticky=E+W) 

text_rne_rro = tk.StringVar()
label_rne_rro = tk.Label(text='rne_rro', font='Verdana 18', bg='cyan')\
    .grid(row=10, column=0, sticky=E)
entry_rne_rro = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_rne_rro)\
    .grid(row=10, column=1, columnspan=1, sticky=E+W) 

text_sealing = tk.StringVar()
label_sealing = tk.Label(text='sealing', font='Verdana 18', bg='cyan')\
    .grid(row=11, column=0, sticky=E)
entry_sealing = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_sealing)\
    .grid(row=11, column=1, columnspan=1, sticky=E+W) 

text_fiscal_number = tk.StringVar()
label_fiscal_number = tk.Label(text='fiscal', font='Verdana 18', bg='cyan')\
    .grid(row=12, column=0, sticky=E)
entry_fiscal_number = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_fiscal_number)\
    .grid(row=12, column=1, columnspan=1, sticky=E+W) 

text_oro_serial = tk.StringVar()
label_oro_serial = tk.Label(text='oro_serial', font='Verdana 18', bg='cyan')\
    .grid(row=13, column=0, sticky=E)
entry_oro_serial = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_oro_serial)\
    .grid(row=13, column=1, columnspan=1, sticky=E+W) 

text_oro_number = tk.StringVar()
label_status = tk.Label(text='oro_num', font='Verdana 18', bg='cyan')\
    .grid(row=14, column=0, sticky=E)
entry_oro_number = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_oro_number)\
    .grid(row=14, column=1, columnspan=1, sticky=E+W) 

text_ticket_serial = tk.StringVar()
label_register = tk.Label(text='tik_serial', font='Verdana 18', bg='cyan')\
    .grid(row=15, column=0, sticky=E)
entry_ticket_serial = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_ticket_serial)\
    .grid(row=15, column=1, columnspan=1, sticky=E+W) 

text_ticket_1sheet = tk.StringVar()
label_ticket_1sheet = tk.Label(text='tik_1sheet', font='Verdana 18', bg='cyan')\
    .grid(row=16, column=0, sticky=E)
entry_ticket_1sheet = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_ticket_1sheet)\
    .grid(row=16, column=1, columnspan=1, sticky=E+W) 

text_ticket_number = tk.StringVar()
label_ticket_number = tk.Label(text='tik_num', font='Verdana 18', bg='cyan')\
    .grid(row=17, column=0, sticky=E)
entry_ticket_number = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_ticket_number)\
    .grid(row=17, column=1, columnspan=1, sticky=E+W) 

#______________________________________

text_sending = tk.StringVar()
label_sending = tk.Label(text='sending', font='Verdana 18', bg='cyan')\
    .grid(row=3, column=2, sticky=E)
entry_sending = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_sending)\
    .grid(row=3, column=3, columnspan=1, sticky=E+W) 

text_books_arhiv = tk.StringVar()
label_books_arhiv = tk.Label(text='book_arh', font='Verdana 18', bg='cyan')\
    .grid(row=4, column=2, sticky=E)
entry_books_arhiv = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_books_arhiv)\
    .grid(row=4, column=3, columnspan=1, sticky=E+W) 

text_tickets_arhiv = tk.StringVar()
label_tickets_arhiv = tk.Label(text='tik_arh', font='Verdana 18', bg='cyan')\
    .grid(row=5, column=2, sticky=E)
entry_tickets_arhiv = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_tickets_arhiv)\
    .grid(row=5, column=3, columnspan=1, sticky=E+W) 

text_to_rro = tk.StringVar()
label_to_rro = tk.Label(text='to_rro', font='Verdana 18', bg='cyan')\
    .grid(row=6, column=2, sticky=E)
entry_to_rro = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_to_rro)\
    .grid(row=6, column=3, columnspan=1, sticky=E+W) 

text_owner_rro = tk.StringVar()
label_owner_rro = tk.Label(text='owner', font='Verdana 18', bg='cyan')\
    .grid(row=7, column=2, sticky=E)
entry_owner_rro = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_owner_rro)\
    .grid(row=7, column=3, columnspan=1, sticky=E+W) 


text_register = tk.StringVar()
label_register = tk.Label(text='register', font='Verdana 18', bg='cyan')\
    .grid(row=8, column=2, sticky=E)
entry_register = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_register)\
    .grid(row=8, column=3, columnspan=1, sticky=E+W) 

text_koatu = tk.StringVar()
label_koatu = tk.Label(text='_koatu_', font='Verdana 18', bg='cyan')\
    .grid(row=15, column=2, sticky=E)
entry_koatu = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_koatu)\
    .grid(row=15, column=3, columnspan=1, sticky=E+W) 

text_tax_id = tk.StringVar()
label_tax_id = tk.Label(text='_tax_id_', font='Verdana 18', bg='cyan')\
    .grid(row=16, column=2, sticky=E)
entry_tax_id = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_tax_id)\
    .grid(row=16, column=3, columnspan=1, sticky=E+W) 


text_koatu2 = tk.StringVar()
label_koatu2 = tk.Label(text='_koatu2_', font='Verdana 18', bg='cyan')\
    .grid(row=17, column=2 ,sticky=E)
entry_koatu = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_koatu2)\
    .grid(row=17, column=3, columnspan=2, sticky=E+W) 


#______________________

text_address = tk.StringVar()
#label_address = tk.Label(text='_address_', font='Verdana 18', bg='cyan')\
#    .grid(row=19, column=0, sticky=E)
entry_address = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_address)\
    .grid(row=19, column=0, columnspan=8, sticky=E+W) 

text_finish = tk.StringVar()
label_finish = tk.Label(text='finish', font='Verdana 18', bg='cyan')\
    .grid(row=9, column=2, sticky=E)
entry_finish = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), textvariable=text_finish)\
    .grid(row=9, column=3, columnspan=1, sticky=E+W) 

#___________________________________________________

#text_box = Text(font=(font_style, font_size), foreground='black', background='cyan')
#text_box.grid(row=19, column=1, columnspan=3, rowspan=1)

text_info = tk.StringVar()
entry_info = tk.Entry(width=WIGHT_ENTRY, font=(font_style, font_size), foreground='blue', textvariable=text_info)\
    .grid(row=21, column=1, columnspan=3, sticky=E+W) 

bigfont = font.Font(family="Helvetica",size=18)
root.option_add("*TCombobox*Listbox*Font", bigfont)

label_model = tk.Label(text='model', font='Verdana 18', bg='cyan')\
    .grid(row=11, column=4, sticky=W)
combo_model = ttk.Combobox(values=get_models())
combo_model.grid(row=11, column=3, sticky=E+W)
combo_model.current(0)
combo_model.bind("<<ComboboxSelected>>", mk_combo_models)


label_combo_soft = tk.Label(text='soft', font='Verdana 18', bg='cyan')\
    .grid(row=12, column=4, sticky=W)
combo_soft = ttk.Combobox(values=get_softs())
combo_soft.grid(row=12, column=3, sticky=E+W)
combo_soft.current(0)
combo_soft.bind("<<ComboboxSelected>>", mk_combo_softs)

label_combo_owner = tk.Label(text='owner', font='Verdana 18', bg='cyan')\
    .grid(row=13, column=4, sticky=W)
combo_owner = ttk.Combobox(values=get_owners())
combo_owner.grid(row=13, column=3, sticky=E+W)
combo_owner.current(0)
combo_owner.bind("<<ComboboxSelected>>", mk_combo_owners)


root.config(menu=main_menu) 
root["bg"] = "cyan"
root.mainloop()