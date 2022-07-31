"""
Created on Sun Jan  2 03:27:20 2022

@author:    Fedi Boukhris: 1535241
            Anis Doudech: 1484190
            Rihab Beshiafi: 1353539
"""

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import GUI_support

#Toplevel enthält Tkinter window , Frames, Canvas, Buttons, Menubar... 
class Toplevel:
    
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
       
        self.konfig = None
        self.konfig_dict = None
        self.image=None
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1284x701")
      #  top.geometry("1084x501")
        top.minsize(176, 1)
        top.maxsize(1284, 701)
        top.resizable(1,  1)
        top.title("GUI")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.my_menu = Menu(self.top)
        self.top.config(menu = self.my_menu)
        self.unter_menu=Menu(self.my_menu, tearoff="off")
        self.my_menu.add_cascade(label = "File",menu=self.unter_menu)
        self.unter_menu.add_command(label = "Konfigurationsdatei Einstellen",
                                    command=lambda: GUI_support.datei_einstellen())
        self.unter_menu.add_command(label = "Anleitung zum Tool Anzeigen ",
                                    command=lambda: GUI_support.anleitung_anzeigen())
        self.unter_menu.add_command(label = "Über uns", 
                                    command=lambda: GUI_support.open_about_us())
        self.unter_menu.add_command(label = "Programm Schließen",
                                     command=lambda: GUI_support.destroy_window(self.top))
        
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.0, rely=0.0, height=71, width=1284)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#575a82")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 20")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Funktionsplotter Tool''')

        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(relx=0.008, rely=0.114, relheight=0.836
                , relwidth=0.984)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.Canvas1 = tk.Canvas(self.TFrame1)
        self.Canvas1.place(relx=0.459, rely=0.017, relheight=0.962
                , relwidth=0.52)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Button1 = tk.Button(self.TFrame1, command= lambda: GUI_support.plot_figure(self))
        self.Button1.place(relx=0.04, rely=0.137, height=42, width=168)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#008080")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Plot Figur''')
        #self.Button1.bind('<Button-1>',lambda e:GUI_support.plot_figure(self))

        self.Button2 = tk.Button(self.TFrame1, command= lambda: GUI_support.on_read_config(self))
        self.Button2.place(relx=0.206, rely=0.034, height=42, width=198)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#008080")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Parameter Zeigen''')
        #self.Button2.bind('<Button-1>',lambda e: GUI_support.on_read_config(self))

        self.Button3 = tk.Button(self.TFrame1, command= lambda: GUI_support.openFile(self))
        self.Button3.place(relx=0.04, rely=0.034, height=42, width=168)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#008080")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Parameter Laden''')
        #self.Button3.bind('<Button-1>',lambda e:GUI_support.openFile(self))

        self.Button4 = tk.Button(self.TFrame1, command= lambda :GUI_support.bild_speichern(self.image))
        self.Button4.place(relx=0.206, rely=0.137, height=42, width=196)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#008080")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button4.configure(foreground="#ffffff")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Figur Speichern''')
       # self.Button4.bind('<Button-1>',lambda e:GUI_support.bild_speichern(self.image))
       
       
        self.Button5 = tk.Button(self.TFrame1, command= lambda :GUI_support.destroy_window(top))
        self.Button5.place(relx=0.15, rely=0.904, height=42, width=178)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#804040")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Button5.configure(foreground="#ffffff")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="#000000")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Schließen''')
       # self.Button5.bind('<Button-1>',lambda e:GUI_support.destroy_window(top))


        self.Canvas2 = tk.Canvas(self.TFrame1)
        self.Canvas2.place(relx=0.009, rely=0.231, relheight=0.663
                   , relwidth=0.438)
        self.Canvas2.configure(background="#d9d9d9")
        self.Canvas2.configure(borderwidth="2")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(relief="ridge")
        self.Canvas2.configure(selectbackground="blue")
        self.Canvas2.configure(selectforeground="white")
        
#Programm starten
if __name__ == '__main__':
    GUI_support.main()




