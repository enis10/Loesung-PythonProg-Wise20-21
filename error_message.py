"""
Created on Sun Jan  2 03:27:20 2022

@author:    Fedi Boukhris: 1535241
            Anis Doudech: 1484190
            Rihab Beshiafi: 1353539
"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self,m):
        super().__init__()
        self.m = m

        # configure the root window
        self.title('Fehlermeldung')
        self.geometry('300x50')

        # label
        self.label = ttk.Label(self, text='Fehler in der Konfigurationsdatei')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='mehr erfahren')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title='Information',
                 message=' Fehler bei '+ self.m)
        self.destroy()


