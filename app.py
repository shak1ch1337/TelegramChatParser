#!/usr/bin/python3


'''--------------------------------------------------
|                                                   |
|                                                   |
|                   TelegramParser                  |
|                     ver.0.1.5                     |
|                                                   |
|                                                   |
|               Created by Shak1ch                  |
|           https://t.me/shak1ch_offc               |
|---------------------------------------------------|'''


from tkinter import *
from tkinter.ttk import *
import webbrowser
from App.telegramParse.parse import start_parsing
import threading
import time


def update_ui(data):    #   Добавление данных в таблицу
    tree.insert("", END, values=data)


def sheduler_parsing(): #   Функция, вызывающая парсинг. Работает рекурсивно
    try:
        data = parse()
        root.after(0, update_ui, data)
    except Exception as e:
        print(f"Ошибка {e}")
    
    root.after(30000, sheduler_parsing)


def parse():    #   Парсинг и форматирование данных
    text = start_parsing()
    text = text.split("\n")
    name = text[0][1:]
    difference = f"{text[1].split(" ")[-2]} {text[1].split(" ")[-1]}"
    price = f"{text[2].split(" ")[-2]} {text[2].split(" ")[-1]}"
    autobuy = f"{text[3].split(" ")[-2]} {text[3].split(" ")[-1]}"
    link = f"https://steamcommunity.com/market/listings/730/{name}"
    data_array = (name, difference, price, autobuy, link)
    return data_array


def open_link_in_browser(event):    #   Открытие ссылки сразу в браузере
    webbrowser.open_new(url=link_source["text"])


def item_selected(event):   #   Функция выделения строки и перенос ссылки на Label
    selected_link = ""
    for items in tree.selection():
        item = tree.item(items)
        i = item["values"]
    link_source["text"] = f"{i[4]}"


#   UI


root = Tk()
root.title("TlegramParser")
root.geometry("1200x800")
root["bg"] = "black"


title = Label(text="Shak1ch-parser", font=("Comic Sans MS", 24), foreground="Green", background="black")
title.pack()
version = Label(text="Version 0.1.4", font=("Comic Sans MS", 11), foreground="Green", background="black")
version.pack()


logo = PhotoImage(file="App/src/images/logo.png")
logoLabel = Label(width=200,  image=logo, border=0)
logoLabel.pack()


link_title = Label(text="Link: ", font=("Comic Sans MS", 14), foreground="white", background="black")
link_title.pack()
link_source = Label(text="", font=("Arial", 9), background="black", foreground="white")
link_source.pack(pady=20)
link_source.bind("<Button-1>", open_link_in_browser)


#   Таблица


columns = ("name", "difference", "price", "autobuy", "link")
tree = Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.heading("name", text="Название:")
tree.heading("difference", text="Цена ниже на:")
tree.heading("price", text="Цена лота:")
tree.heading("autobuy", text="Автобай:")
tree.heading("link", text="Ссылка:")


tree.column("#1", stretch=NO, width=300)
tree.column("#2", stretch=NO, width=120)
tree.column("#3", stretch=NO, width=120)
tree.column("#4", stretch=NO, width=170)
tree.column("#5", stretch=NO, width=500)


tree.bind("<<TreeviewSelect>>", item_selected)


root.after(0, sheduler_parsing)


root.mainloop()