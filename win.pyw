from tkinter import *
from typing import Any

from modules import *
from papa_pg import *


def clear_me():
    text_box.delete(1.0, END)

def say(txt):
    text_box.delete(1.0, END)
    text_box.insert(1.0, str(txt))


def edit_show():
    key_item = str(text_box.get(1.0, END)).strip()
    clear_me()
    try:
        text_box.insert(1.0, mk_txt(key_item))
    except:
        pass

def edit_add_dep():
    txt = text_box.get(1.0, END).strip()
    vec = get_data_from_textbox(txt)
    try:
        refresh_one_dep(vec)
        say(f'{vec[0]}')
    except Exception as ex:
        clear_me()
        say(ex)

def edit_add_term():
    txt = text_box.get(1.0, END).strip()
    vec = get_data_from_textbox(txt)
    refresh_one_term(vec)
    try:
        refresh_one_term(vec)
            #say(f'{vec[1]}')
        #say(str(vec))
    except Exception as ex:
        pass
        #clear_me()
        #say(vec)

 


font_size = 18
font_style = "Verdana"

root = Tk()
main_menu = Menu(root)

font_size = 18
term_size = len(file_to_arr(IN_DATA_PATH + "terminals.csv")[0])
dep_size = len(file_to_arr(IN_DATA_PATH + "departments.csv")[0])

edit_memu = Menu(main_menu, tearoff=0)
edit_memu.add_command(label="show", command=edit_show, font=(font_style, font_size))
edit_memu.add_command(label="add_dep", command=edit_add_dep, font=(font_style, font_size))
edit_memu.add_command(label="add_term", command=edit_add_term, font=(font_style, font_size))
edit_memu.add_command(label="clear", command=clear_me, font=(font_style, font_size))

main_menu.add_cascade(label="edit",
                     menu=edit_memu)


text_box = Text(font=(font_style, font_size), foreground='black', background='cyan')
text_box.pack(side=LEFT, fill=BOTH)

root.config(menu=main_menu)

f = Frame()
f.pack(side=LEFT, padx=10)

root["bg"] = "cyan"
root.mainloop()