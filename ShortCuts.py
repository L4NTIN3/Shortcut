from os import symlink
import tkinter as tk
from tkinter import *
from tkinter.constants import CENTER, E, RIGHT, Y
import webbrowser
import subprocess

# ---------- Tommi Virtanen 2021 -----------
# Just a little try out of Python during summer. Got it to work, gonna make some changes some day.
# The idea was to make and expandable "shortcutter" for my Linux system. Ended up not making it very easily expandable but works tho.

#set size, name and overall make the window
window = tk.Tk()
window.title("ShortCutz")
window.geometry("300x200")

canvas1 = tk.Canvas(window, width=300, height=100)
canvas1.pack()
canvas1.configure(bg ="pink")

canvas2 = tk.Canvas(window, width=300, height=100)
canvas2.pack()
canvas2.configure(bg="cyan")

vs = "/var/lib/snapd/snap/bin/code"
discord = "/var/lib/snapd/snap/bin/discord"

def checkInput():
    input = syöte.get()

    inputs = ["youtube", "Youtube", "samk", "Samk", "SAMK", "reddit", "Reddit", "code", "VS", "Visual Studio Code", "discord", "Discord", "listaa", "Listaa"]

    if input == "youtube" or input == "Youtube":
        openYoutube()
    elif input == "samk" or input == "SAMK" or input == "Samk":
        openSAMK()
    elif input == "reddit" or input == "Reddit":
        openReddit()
    elif input == "code" or input == "VS" or input == "Visual Studio Code":
        openVS()
    elif input == "discord" or input == "Discord":
        openDiscord()
    elif input == "listaa" or input == "Listaa":
        openCommands()
    else:
        pass



def openSAMK():
    webbrowser.open("https://www.samk.fi/")

def openYoutube():
    webbrowser.open("https://www.youtube.com/")

def openReddit():
    webbrowser.open("https://www.reddit.com/")

def openVS(): 
    subprocess.Popen([vs])

def openDiscord():
    subprocess.Popen([discord])


def openCommands():
    komennot = tk.Tk()
    komennot.geometry("200x200")
    komennot.title("commands")

    canvas3 = tk.Canvas(komennot, width=200, height=200)
    lista = Label(komennot, text="Youtube \n Samk \n Reddit \n Visual Studio \n Discord")
    canvas3.pack()
    lista.place(relx = 0.5, rely=0.5, anchor=CENTER)

    canvas3.create_window(50, 50, window=lista)


#make the button

#openButton = tk.Button(window, text="Avaa sovellus")
#openButton.pack()

#Make the input bar
syöte = tk.Entry(window)
#create canvas to put things in
canvas1.create_window(200, 140, window=syöte)
syöte.place(relx = 0.5, rely=0.25, anchor=CENTER)
openButton = tk.Button(window, text="Avaa sovellus", padx=40, pady=15, command=checkInput)

canvas2.create_window(150, 100, window=openButton)
openButton.place(relx = 0.5, rely=0.75, anchor=CENTER)


window.mainloop()
