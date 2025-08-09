#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *
import webbrowser


def start_parsing():
    pass

root = Tk()
root.title("Shak1chTlegramParser")
root.geometry("1200x800")


def open_link_in_browser(event):
    webbrowser.open_new(url=link_source["text"])


def test2():
    link_source["text"] = "test"


def item_selected(event):
    selected_link = ""
    for items in tree.selection():
        item = tree.item(items)
        i = item["values"]
    link_source["text"] = f"{i[4]}"


title = Label(text="Shak1ch-parser", font=("Arial", 32), foreground="Green")
title.pack()
version = Label(text="Version 0.1.1", font=("Arial", 14), foreground="Green")
version.pack()


link_title = Label(text="Link: ", font=("Calibri", 16))
link_title.pack(pady=20)
link_source = Label(text="", font=("Arial", 16))
link_source.pack(pady=20)
link_source.bind("<Button-1>", open_link_in_browser)



#   Таблица

item = ("MAC-10 | Last Dive (Field-Tested)", "14.03%", "200.00 RUB", "228.07 RUB", "https://steamcommunity.com/market/listings/730/MAC-10 | Last Dive (Field-Tested)")


columns = ("name", "difference", "price", "autobuy", "link")
tree = Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.heading("name", text="Название:")
tree.heading("difference", text="Цена ниже на:")
tree.heading("price", text="Цена лота:")
tree.heading("autobuy", text="Автобай:")
tree.heading("link", text="Ссылка:", command=test2)

tree.column("#1", stretch=NO, width=300)
tree.column("#2", stretch=NO, width=120)
tree.column("#3", stretch=NO, width=120)
tree.column("#4", stretch=NO, width=170)
tree.column("#5", stretch=NO, width=500)

tree.insert("", END, values=item)
tree.bind("<<TreeviewSelect>>", item_selected)


root.mainloop()