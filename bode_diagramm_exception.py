"""
Created on Sun Jan  2 03:27:20 2022

@author:    Fedi Boukhris: 1535241
            Anis Doudech: 1484190
            Rihab Beshiafi: 1353539
"""

from tkinter import *
import tkinter as tk
import re


def validate(string):
    regex = re.compile(r"(\+|\-)?[0-9./*+()s-]*$")
    result = regex.match(string)
    return (string == ""
            or (string.count('+') <= 12

                and string.count('.') <= 12
                and result is not None
                and result.group(0) != ""))


def on_validate(P):
    return validate(P)



window = tk.Tk()
window.title("g(s) error")


entry = tk.Entry(window, validate="key")

vcmd = (entry.register(on_validate), '%P')
entry.config(validatecommand=vcmd)
entry.pack()


def submit():
    global g_s

    a= entry.get()

    g_s = str(a)
    window.destroy()


button = Button(window,text = "submit",command =submit )
button.pack()
window.mainloop()

print(g_s)
