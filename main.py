# Code by: Robatortas / NoFall

from pytube import YouTube

import PySimpleGUI as gui

title = "Coffee Beans"
font = ("Cascadia Code", 40)
margins = (50, 50)

backgroundColor = '#6D5D46'
gui.theme = backgroundColor

buttonColor = '#917B5D'

layout = [[gui.Text("Coffee Beans", size=(0, 0), key="TITLE", font=font, background_color=backgroundColor)], [gui.Text("Save path", background_color=backgroundColor)], [gui.In(size=(25, 1), enable_events=True, key="CHOSEN_PATH"), gui.FolderBrowse(button_color=buttonColor, key="BROWSE")]]
window = gui.Window(title, layout, margins=margins, background_color=backgroundColor)

class Script:
    while True:
        event, values = window.read()
        if(event == "Exit" or event == gui.WINDOW_CLOSED): break

        if(event == "BROWSE"):
            print("BROWSE")
            window["CHOSEN_PATH"].update(window["CHOSEN_PATH"].get() + "Hey")