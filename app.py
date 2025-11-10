#!/usr/bin/python3

#   Importing libraries

from tkinter import *
from tkinter.ttk import *
import webbrowser
from app.controllers.parser import startParsing
import pygame


'''
ㄒ🝗㇄🝗Ꮆ尺闩爪
尸闩尺丂🝗尺
𝘷𝘦𝘳𝘴𝘪𝘰𝘯 0.1.9

丂卄闩长丨⼕卄
'''


#   Functions for work!


def playSound(file):    #   Fucntion for play message-sound
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def updateUI(data): #   Insert formated data in table
    tree.insert("", END, values = data)


def openLinkInBrowser(event):   #   Open links on browser
    webbrowser.open_new(url = link["text"])


def shedulerParsing():  #   Recursing function. Start parsing every 30s
    try:
        data = parseTelegramChannel()
        window.after(0, updateUI, data)
        playSound("app/src/message.mp3")
        print(data) #   Check message
    except Exception as e:
        print(f"Error {e}") #   Check errors
    window.after(30000, shedulerParsing)


def parseTelegramChannel(): #   Getting and formatting message
    response = startParsing()
    all_text = response.split("\n")


    #   Formated data

    name = all_text[0][1:]
    difference = all_text[1][1:]
    price = all_text[2][1:]
    autobuy = all_text[3][1:]
    link = f"https://steamcommunity.com/market/listings/730/{name}"
    data_array = (name, difference, price, autobuy, link)


    return data_array


def tableItemsSeelcted(event):  #   Output link from table
    for items in tree.selection():
        item = tree.item(items)
        table_link = item["values"]
    link["text"] = f"{table_link[4]}"


#   User-Interface


window = Tk()
window.title("Telegram Parser")
window.geometry("1200x800")
window["bg"] = "black"


logo = Label(text = "Telegram Parser", background="black", foreground="green", font=("Calibri", 22))
logo.pack(pady=20)


link = Label(text = "https://github.com/shak1ch1337/", background="black", foreground="white", font=("Calibri", 16))
link.pack(pady=10)
link.bind("<Button-1>", openLinkInBrowser)


columns = ("name", "difference", "price", "autobuy", "link")
tree = Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.heading("name", text="Название:")
tree.heading("difference", text="Цена ниже на:")
tree.heading("price", text="Цена лота:")
tree.heading("autobuy", text="Автобай:")
tree.heading("link", text="Ссылка:")


tree.bind("<<TreeviewSelect>>", tableItemsSeelcted) #   Seelcted item from table


window.after(0, shedulerParsing)    #   Start recursive pars-function


window.mainloop()