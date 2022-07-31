"""
Created on Sun Jan  2 03:27:20 2022

@author:    Fedi Boukhris: 1535241
            Anis Doudech: 1484190
            Rihab Beshiafi: 1353539
"""


import tkinter as tk
import Check_Konfiguration
import GUI_main
import plot_messdaten as pm
from PIL import ImageTk,Image 
from tkinter import filedialog
import os.path
import os


#Methode zum Starten des Programms 
def main(*args):
    
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global window
    window = GUI_main.Toplevel(root)
    root.mainloop()
    

#Erstellen eines Strings aus einem Dictionary
def config_to_string(config_dict):
    result = ""
    for key, value in config_dict.items():
        result += f"{key}:\t {value}\n"
       
    return result

#Anzeigen der Konfigurationsdaten auf dem GUI
def on_read_config(tks):
        if tks.konfig_dict==None:
            print('Parameter können nicht angezeigt werden, Bitte Laden Sie erstmal die Konfig-Datei hoch')
        else:
            tks.Canvas2.delete("all")
            tks.Canvas2.create_text(200,  200, text=config_to_string(tks.konfig_dict), 
                                    fill="black", font=('Helvetica 9 bold'),  justify="left")

#Anzeigen des Figures auf dem GUI
def plot_figure(tks):
    if tks.konfig==None:
        print('Funktion kann nicht geplottet werden, Bitte Laden Sie erstmal die Konfig-Datei hoch')
    else:
        s= tks.konfig.getCheck()
        if s=='messdaten':
            plot_messdaten=pm.Plot_messdaten(tks.konfig_dict)
            img= plot_messdaten.plot_figure()
            img=Image.fromarray(img)
            tks.image = img.resize((657,552), Image.ANTIALIAS)
        
        elif s=='funktionsgleichung':
            plot_fuktionsgleichung=pm.Plot_fuktionsgleichung(tks.konfig_dict)
            img= plot_fuktionsgleichung.plot_figure()
            img=Image.fromarray(img)
            tks.image= img.resize((657,552), Image.ANTIALIAS)
        
        elif s=='parametrisch':
            plot_param_fuktionsgleichung=pm.Plot_param_funktion(tks.konfig_dict)
            img= plot_param_fuktionsgleichung.plot_figure()
            img=Image.fromarray(img)
            tks.image= img.resize((657,552), Image.ANTIALIAS)
        
        elif s=='mehredimensionalefunktion':
            plot_3d=pm.Mehredimensionalefunktion(tks.konfig_dict)
            img= plot_3d.plot_figure()
            img=Image.fromarray(img)
            tks.image= img.resize((657,552), Image.ANTIALIAS)
        
        else :
            plt_uf = pm.Uebertragungsfunktion(tks.konfig_dict)
            img= plt_uf.plot_bode_diagram()
            img=Image.fromarray(img)
            tks.image= img.resize((657,500), Image.ANTIALIAS)
         
        
        
        img =ImageTk.PhotoImage(tks.image)
        
        tks.Canvas1.create_image(328, 255, image=img, anchor='center')    
        #frame.Canvas1.update()
        tks.top.mainloop()
       
        
#Programm schließen
def destroy_window(tks):
    tks.destroy()
   

#Konfigurationsdaten Laden
def openFile(tks):
    filename = filedialog.askopenfilename(filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    ))  
    tks.konfig = Check_Konfiguration.Check_konfiguration(filename) 
    tks.konfig_dict = tks.konfig.fill_keys()
    

#Figure als png speicehrn      
def bild_speichern(image):
    if (not (image==None)):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".png", 
                                    filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
        if file:
            abs_path = os.path.abspath(file.name)
            image.save(abs_path)
    else:
        print('Sie haben noch keine Funktion geplottet')

#Konfigurationsdatei ändern    
def datei_einstellen():
    filename = filedialog.askopenfilename(filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )) 
    
    os.startfile(filename)

#Bedienungsanleitung Anzeigen
def anleitung_anzeigen():
    os.startfile('bericht.pdf')

#Öffnen von Über uns html Seite    
def open_about_us():
    os.startfile('about us\index.html')




