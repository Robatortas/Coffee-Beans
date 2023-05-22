# Code by: Robatortas / NoFall

from pytube import YouTube

import PySimpleGUI as gui

class Interface:
    title = "Coffee Beans"
    font = ("Cascadia Code", 40)
    margins = (50, 50)

    backgroundColor = '#6D5D46'
    gui.theme = backgroundColor

    buttonColor = '#917B5D'

    layout = [[gui.Text("Coffee Beans", size=(0, 0), key="TITLE", font=font, background_color=backgroundColor)], [gui.Text("Save path", background_color=backgroundColor)], [gui.In(size=(25, 1), enable_events=True, key="CHOSEN_PATH")], [gui.FolderBrowse(button_color=buttonColor, key="BROWSE")]]


    gui.Window(title, layout, margins=margins, background_color=backgroundColor).read()

class Script:
    while True:
        event, values = gui.Window.read()
        if(event == "BROWSE"):
            values["CHOSEN_PATH"] 