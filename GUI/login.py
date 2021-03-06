import sys
import spotipy
import spotipy.util as util
import tkinter as tk 
from tkinter import *
from PIL import ImageTk,Image
from tkinter import font

login = Tk()
login.title("Welcome to Moodipy!")
login.configure(bg = "black")
login.resizable(width = False, height = False)
login.geometry("900x600")

B = Button(login,
    text = "Login with Spotify",
    bg ="green",
    font = "Helvetica 20 bold italic",
    bd = 6, relief = "raised",
    width = 25,
    height = 2)
B.place(x = 225,y = 480)

canvas = Canvas(login, width = 850, height = 460)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("./GUI/snake.png"))
canvas.create_image(20, 20, anchor=NW, image=img) 

login.mainloop()

