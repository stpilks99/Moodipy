import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
import os

from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import ImageTk,Image

ep = Tk()
ep.title("View Playlist")
ep.configure(bg = "black")
ep.resizable(width = False, height = False)
ep.geometry("900x680")

# Function called when logout button pressed
def logout():
    sys.exit()

# Playlist title label
t = Label(ep, text = '        Playlist Title        ',  fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 40 bold italic")
t.place(x = 250, y = 50)

# Sidebar buttons
# Home
h = Button(ep,
    text = "Home",
    bg ="green", bd = 6,
    relief = "raised",
    width = 24,
    height = 4)
h.place(x = 0, y = 0)

# Logout
lo = Button(ep,
    text = "Logout",
    command = logout,
    bg ="green", bd = 6,
    relief = "raised", width = 24,
    height = 4)
lo.place(x = 0, y = 80)

# Help/Doc
hd = Button(ep,
    text = "Help/Doc",
    bg ="green", bd = 6,
    relief = "raised",
    width = 24,
    height = 4)
hd.place(x = 0, y = 160)

# Edit/Options
add = Button(ep,
    text = "Add\nSong",
    bg ="green", bd = 6,
    relief = "raised",
    width = 11,
    height = 4)
add.place(x = 0, y = 240)

rem = Button(ep,
    text = "Remove\nSong",
    bg ="green", bd = 6,
    relief = "raised", width = 11,
    height = 4)
rem.place(x = 90, y = 240)

rank = Button(ep,
    text = "Rank\nSong",
    bg ="green", bd = 6, 
    relief = "raised",
    width = 11,
    height = 4)
rank.place(x=0, y = 320)

de = Button(ep,
    text = "Delete\nPlaylist",
    bg ="green",
    bd = 6,
    relief = "raised",
    width = 11,
    height = 4)
de.place(x = 90, y =320 )

# Songs
fields = Label(ep, text = '       Song               Artist           Album                 ', fg = "black", bg = "green", bd = 6, relief = "sunken", font = "Helvetica 18 bold italic")
fields.place(x = 250, y = 150)

listbox = Listbox(ep, bg = "gray", height = 10, width = 49, bd = 6, relief = "sunken", font = "Helvetica 15 bold italic") 
listbox.pack(side = RIGHT, fill = BOTH) 
listbox.place(x = 250, y = 300)
scrollbar = Scrollbar(ep) 

for values in range(100): 
    listbox.insert(END, values) 

listbox.config(yscrollcommand = scrollbar.set) 
scrollbar.config(command = listbox.yview) 

ep.mainloop()