#Todo
#   make a TKinter window
#   in a simple way, create a basic scrolling selection that works on different sized screens
#   figure out how best to have menu call software, issolate menu options to another file.  name and filepath
#   seperate out keystrokes so it will work with either keyboard arrows, gaming remote, or gpio pins


import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import ttk


def button1 ():
    top = Toplevel()

    listbox = Listbox(top)
    listbox.grid()
    listbox.insert(END, "a list entry")

    for item in ["one", "two", "three", "four"]:
        listbox.insert(END, item)

    b = Button(top, text="enter", command=lambda listbox=listbox: listbox.delete(ANCHOR)).grid()
    Listbox.activate(END)

def button2 ():
    print("what")


def button3 ():
    print("what")


def button4 ():
    print("what")

def button5 ():
    print("what")

def enterbutton():
    print("Thingy")

root=Tk()
root.geometry("640x480")
#top = Toplevel()

ttk.Button(root, text="button1", command=button1).grid()
ttk.Button(root, text="button2", command=button2).grid()
ttk.Button(root, text="button3", command=button3).grid()
ttk.Button(root, text="button4", command=button4).grid()
ttk.Button(root, text="button5", command=button5).grid()
ttk.Button(root, text="Exit", command=quit).grid()

root.mainloop() #keeps program running until we close
