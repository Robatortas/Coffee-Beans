# Code by: Robatortas / NoFall

import os
import sys
import PySimpleGUI as gui

from pytube import YouTube
from pytube.exceptions import ExtractError

title = "Coffee Beans"
font = ("Cascadia Code", 40)
margins = (50, 50)

backgroundColor = '#6D5D46'
gui.theme = backgroundColor

buttonColor = '#917B5D'
layout = [[gui.Text("Coffee Beans", size=(0, 0), key="TITLE", font=font, background_color=backgroundColor)], 
          [gui.Text("Link", background_color=backgroundColor)], 
          [gui.In(size=(25, 1), enable_events=True, key="LINK")], 
          [gui.Text("Download path", background_color=backgroundColor)], 
          [gui.In(size=(25, 1), enable_events=True, key="CHOSEN_PATH"), gui.FolderBrowse(button_color=buttonColor, key="BROWSE")],
          [gui.Button("DOWNLOAD", button_color='#CA8957')]]

window = gui.Window(title, layout, margins=margins, background_color=backgroundColor)

class Script:

    def warning(title, text):
        layoutWarn = [[gui.Text(text, key="WARNING_WIN", background_color=backgroundColor)], [gui.Button("Ok", key="OK_WARN")]]

        window = gui.Window(title, layoutWarn, modal=True, background_color=backgroundColor)

        while True:
            event, values = window.read()

            if event == "Exit" or event == gui.WIN_CLOSED or event == "OK_WARN":
                break

        window.close()

    while True:
        event, values = window.read()
        if(event == "Exit" or event == gui.WINDOW_CLOSED): break
        
        chosenPath = str(values["CHOSEN_PATH"])

        if(event == "DOWNLOAD"):
                while(os.path.exists(chosenPath)):
                    downloadLink = values['LINK']

                    try:
                        window.set_title(title + " || CONVERTING")
                        yt = YouTube(downloadLink)
                        warning("WARNING", "WARNING: The program will freeze, that's okay!\nDon't fret, I am working hard on converting your video.")
                        print("var downloadLink = " + downloadLink)
                        print("\nCONVERTING AND DOWNLOADING\n")
                        yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(chosenPath)
                    except ExtractError:
                        print("\nERROR: INVALID YOUTUBE LINK\n")
                        warning("ERROR", "ERROR: INVALID YOUTUBE LINK.\n\nPLEASE PROMPT A VALID ONE.")
                    
                    break
                else: 
                    print("\nERROR: INVALID DOWNLOAD PATH\n")
                    warning("ERROR", "ERROR: INVALID DOWNLOAD PATH.\n\nPLEASE PROMPT A VALID ONE.")