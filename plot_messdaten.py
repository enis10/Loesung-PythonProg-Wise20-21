"""
Created on Sun Jan  2 03:27:20 2022

@author:    Fedi Boukhris: 1535241
            Anis Doudech: 1484190
            Rihab Beshiafi: 1353539
"""

import matplotlib.pyplot as plt
from matplotlib.colors import is_color_like
import numpy as np
import cmath


#Plot_messdaten plottet eine Reihe von Werten
class Plot_messdaten:
    
     def __init__(self, param_dict): 
         self.x_reihe= param_dict['x_reihe']
         self.y_reihe= param_dict['y_reihe']
         self.grid= param_dict['grid']
         self.color= param_dict['color']
         self.linewidth= param_dict['linewidth']
         self.linestyle= param_dict['linestyle']
         #self.legend= param_dict['legend']
         self.x_label= param_dict['x_label']
         self.y_label= param_dict['y_label']
         self.title=param_dict['title']
         
         
     def plot_figure(self):
        fig= plt.figure(figsize=(8, 8))
        
        #Farbe überprüfen
        if not(is_color_like(self.color)):
            self.color= 'blue'
            print('Linienfarbe wurde nicht erkannt, Linienfarbe wurde auf Blaue eingestellt')
        
        if not (self.linestyle in ['-', '--', '-.', ':', 'solid', 'dashed', 
                                   'dashdot', 'dotted']):
            self.linestyle= None
            print('Linestyle wurde nicht erkannt, Liniestyle wurde auf default eingestellt')
        
        plt.plot(self.x_reihe, self.y_reihe, color=self.color, linestyle=self.linestyle,linewidth = self.linewidth)
        plt.grid(self.grid)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        
        fig.canvas.draw()  
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.clf()
        
        return img

#Plot_fuktionsgleichung plottet eine oder mehrere Funktionen f(x)
class Plot_fuktionsgleichung:

    def __init__(self, param_dict):

        self.f_1 = param_dict['f_1(x)']
        self.f_2 = param_dict['f_2(x)']
        self.f_3 = param_dict['f_3(x)']
        self.x_start = param_dict['x_start']
        self.x_end = param_dict['x_end']
        self.x_step = param_dict['x_step']
        self.grid = param_dict['grid']
        self.color_1 = param_dict['color_1']
        self.color_2 = param_dict['color_2']
        self.color_3 = param_dict['color_3']
        self.linewidth_1 = param_dict['linewidth_1']
        self.linewidth_2 = param_dict['linewidth_2']
        self.linewidth_3 = param_dict['linewidth_3']
        self.linestyle_1 = param_dict['linestyle_1']
        self.linestyle_2 = param_dict['linestyle_2']
        self.linestyle_3 = param_dict['linestyle_3']
        self.title = param_dict['title']
        self.legend = param_dict['legend']
        self.x_label = param_dict['x_label']
        self.y_label = param_dict['y_label']

    #Berechnen von x und y Werten
    def funktion(self, s):
        bereich = np.arange(self.x_start, self.x_end + 1, self.x_step)
        y_axe = np.zeros(len(bereich), dtype=float)
        i = 0
        for x in bereich:
            f = eval(s, {"x": x})
            y_axe[i] = f
            i += 1
        return bereich, y_axe

    def plot_figure(self):
        fig=plt.figure(figsize=(8, 8))
        if (self.f_1 != ""):
            self.plot_function(self.f_1, self.color_1, self.linestyle_1,
                               self.linewidth_1, self.f_1)
        if (self.f_2 != ""):
            self.plot_function(self.f_2, self.color_2, self.linestyle_2,
                               self.linewidth_2, self.f_3)

        if (self.f_3 != ""):
            self.plot_function(self.f_3, self.color_3, self.linestyle_3,
                               self.linewidth_3, self.f_2)
        plt.grid(self.grid)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        if self.legend:
            plt.legend()    
        fig.canvas.draw()  
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.clf()
        
        return img
    
    def plot_function(self, func, color, linestyle, linewidth, label):

        # Farbe überprüfen
        #color= color
        if not (is_color_like(color)):
            color = 'blue'
            print('Linienfarbe wurde nicht erkannt, Linienfarbe wurde auf Blaue eingestellt')

        # Linestyle überprüfen
        if not (linestyle in ['-', '--', '-.', ':', 'solid', 'dashed', 'dashdot',
                              'dotted']):
            linestyle = None
            print('Linestyle wurde nicht erkannt, Linestyle wurde auf default eingestellt')

        x_axe, y_axe = self.funktion(func)
        plt.plot(x_axe, y_axe, label=label, color=color, linestyle=linestyle, linewidth= linewidth)


#Plot_param_funktion plottet eine parametrische Funktionen f(x,a,b), wobei sind a und b die Parameter 
class Plot_param_funktion:
    
    def __init__(self, param_dict): 
        self.f_parametriert= param_dict['f_parametriert(x,a,b)']
        self.a= param_dict['a'] 
        self.b= param_dict['b'] 
        self.x_start= param_dict['x_start'] 
        self.x_end= param_dict['x_end']
        self.x_step= param_dict['x_step']
        self.grid= param_dict['grid']
        self.color= param_dict['color']
        self.linewidth= param_dict['linewidth']
        self.linestyle= param_dict['linestyle']
        self.x_label= param_dict['x_label']
        self.y_label= param_dict['y_label']
        self.title= param_dict['title']
        
    #Berechnen von x und y Werten
    def funktion_param(self, s):
         bereich = np.arange(self.x_start, self.x_end+1, self.x_step)
         y_axe= np.zeros(len(bereich),dtype=float)
         i=0
         for x in bereich:
            f = eval(s, {"x":x, "a":self.a, "b":self.b})
            y_axe[i] = f 
            i+=1
    
         return bereich, y_axe
    
    
    def plot_figure(self):
        
        fig=plt.figure(figsize=(8, 8))
        
        #Farbe überprüfen
        if not(is_color_like(self.color)):
            self.color= 'blue'
            print('Linienfarbe wurde nicht erkannt, Linienfarbe wurde auf Blaue eingestellt')
        
        if not (self.linestyle in ['-', '--', '-.', ':', 'solid', 'dashed', 
                                   'dashdot', 'dotted']):
            self.linestyle= None
            print('Linestyle wurde nicht erkannt, Liniestyle wurde auf default eingestellt')
        
        x_axe, y_axe= self.funktion_param(self.f_parametriert)
        plt.plot(x_axe, y_axe, color=self.color, linestyle=self.linestyle, linewidth = self.linewidth)
        plt.grid(self.grid)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        fig.canvas.draw()  
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.clf()
        
        return img

#Mehredimensionalefunktion plottet eine 2-D Funktion z = f(x,y) als 3d-plot
class Mehredimensionalefunktion:
    
    def __init__(self, param_dict): 
        self.f_3d= param_dict['f_3d(x,y)']
        self.start= param_dict['start'] 
        self.end= param_dict['end'] 
        self.step= param_dict['step']
        self.grid= param_dict['grid']
        self.color= param_dict['color']
        self.linewidth= param_dict['linewidth']
        self.linestyle= param_dict['linestyle']
        self.x_label= param_dict['x_label']
        self.y_label= param_dict['y_label']
        self.z_label= param_dict['z_label']
        self.title= param_dict['title']       
        
    #Berechnen von x und y Werten
    def funktion_3d(self, s):
         bereich = np.arange(self.start, self.end+1, self.step)
         z_axe= np.zeros(len(bereich),dtype=float)
         i=0
         for x in bereich:
            f = eval(s, {"x":x, "y":x})
            
            z_axe[i] = f 
            i+=1
            
         return bereich, z_axe
     
     
    def plot_figure(self):
        
        fig=plt.figure(figsize=(8, 8))
        ax=fig.add_subplot(111,projection='3d')
        #Farbe überprüfen
        if not(is_color_like(self.color)):
            self.color= 'blue'
            print('Linienfarbe wurde nicht erkannt, Linienfarbe wurde auf Blaue eingestellt')
        
        if not (self.linestyle in ['-', '--', '-.', ':', 'solid', 'dashed', 
                                   'dashdot', 'dotted']):
            self.linestyle= None
            print('Linestyle wurde nicht erkannt, Liniestyle wurde auf default eingestellt')
        
        bereich, z_axe= self.funktion_3d(self.f_3d)
        ax.plot(bereich, bereich, z_axe, color=self.color, linestyle=self.linestyle, linewidth= self.linewidth)
        plt.grid(self.grid)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        
        fig.canvas.draw()  
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.clf()
        
        return img

#Uebertragungsfunktion plottet das Bodediagramm einer Übertragungsfunktion G(s)
class Uebertragungsfunktion:

    def __init__(self, param_dict):
        self.g_s = param_dict['g(s)']
        self.f_start = param_dict['f_start']
        self.f_end = param_dict['f_end']

        self.grid = param_dict['grid']
        self.color = param_dict['color']
        self.linewidth = param_dict['linewidth']
        self.linestyle = param_dict['linestyle']

    #Berechnen von Amplitudengangs-, Phasengang-, und frequenzwerten
    def prepare(self):
        eq = self.g_s
        freq = np.linspace(self.f_start,self.f_end, 200)
        Amplitudengang_db = np.zeros(len(freq), dtype=float)
        Phasengang_rad = np.zeros(len(freq), dtype=float)
        for i in range(len(freq)):

            s = complex(0, 2 * np.pi * freq[i])
            try :

                H = eval(eq, {"s": s})
            except :
                import bode_diagramm_exception as be
                eq = be.g_s
            H = eval(eq, {"s": s})
            Amplitudengang_db[i] = 20 * np.log10(abs(H))
            Phasengang_rad[i] = ((cmath.phase(H) * 180) / np.pi)
        return Amplitudengang_db, Phasengang_rad, freq


    def plot_bode_diagram(self):
        ag_db,ph_rad,freq = self.prepare()
        fig=plt.figure(figsize=(8, 8))
        plt.subplot(2, 1, 1)
        if not (is_color_like(self.color)):
            self.color = 'blue'
            print('Linienfarbe wurde nicht erkannt, Linienfarbe wurde auf Blaue eingestellt')

        if not (self.linestyle in ['-', '--', '-.', ':', 'solid', 'dashed',
                                   'dashdot', 'dotted']):
            self.linestyle = None
            print('Linestyle wurde nicht erkannt, Liniestyle wurde auf default eingestellt')
        plt.semilogx(freq, ag_db,color = self.color, linestyle = self.linestyle,linewidth = self.linewidth)

        plt.grid(self.grid)
        plt.xlabel('Frequenz in Hz')
        plt.ylabel('Amplitudengang in dB')

        plt.subplot(2, 1, 2)
        plt.semilogx(freq, ph_rad,color = self.color, linestyle = self.linestyle,linewidth = self.linewidth)
        plt.grid(self.grid)

        plt.xlabel('Frequenz in Hz')
        plt.ylabel('Phasengang in deg')

        plt.tight_layout()
      
        fig.canvas.draw()  
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        plt.clf()
        
        return img
           