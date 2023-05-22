# Code by: Robatortas / NoFall

from pytube import YouTube

import PySimpleGUI as gui

class Interface:
    title = "Coffee Beans"
    font = ("Cascadia Code", 40)

    backgroundColor = '#ff00ff'
    layout = [[gui.Text("Coffee Beans", size=(0, 0), key="-text-", font=font)], [gui.Text("Save path")], [gui.In(size=(25, 1), enable_events=True, key="-CHOSEN_PATH-")], [gui.FolderBrowse()]]

    margins = (200, 50)


    gui.Window(title, layout, margins=(200, 200), background_color=backgroundColor).read()



