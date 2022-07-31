"""
Created on Sun Jan  2 03:27:20 2022

@author:    Fedi Boukhris: 1535241
            Anis Doudech: 1484190
            Rihab Beshiafi: 1353539
"""

#Klasse für Einlesen und Vorbereiten von Konfigurationsdaten
class Check_konfiguration :
    #Attributen initialisieren
    def __init__(self, filename=None):
        #Array enthält mögliche Typen von zu plottenden Funktion
        self.funktionstype = ['messdaten', 'funktionsgleichung', 'parametrisch',
                         'mehredimensionalefunktion', 'uebertragungsfunktion']
        
        #passende Dictionary für jeden Funktionstyp, enthält Die Konfigurationsdaten 
        #mit den dazu gehörigen Schlüssel
        self.messdaten_dict = {'x_reihe': [], 'y_reihe': [], 'title': '', 'grid': bool, 'color': '',
                          'linewidth': float, 'linestyle': '', 'x_label': '', 'y_label': ''}

        self.func_dict = {'f_1(x)': '', 'f_2(x)': '', 'f_3(x)': '', 'x_start': float, 'x_end': float,
                     'x_step': float, 'grid': bool, 'color_1': '', 'color_2': '', 'color_3': '',
                     'linewidth_1': float, 'linewidth_2': float, 'linewidth_3': float,
                     'linestyle_1': '', 'linestyle_2': '', 'linestyle_3': '', 'title': '',
                     'legend': bool, 'x_label': '', 'y_label': ''}

        self.param_func_dict = {'f_parametriert(x,a,b)': '', 'a': float, 'b': float, 'x_start': float,
                           'x_end': float, 'x_step': float, 'grid': bool, 'color': '', 'linewidth': float,
                           'linestyle': '', 'title': '', 'x_label': '', 'y_label': ''}

        self.func_3D_dict = {'f_3d(x,y)': '', 'start': float, 'end': float, 'step': float, 'grid': bool,
                        'color': '', 'linewidth': float, 'linestyle': '', 'x_label': '', 'y_label': '',
                        'z_label': '', 'title': ''}

        self.func_ubertragung_dict = {'g(s)': '', 'f_start': float, 'f_end': float, 'grid': bool, 'color': '',
                                 'linewidth': float, 'linestyle': ''}
        
        #Pfad von der Konfigurationsdatei
        self.filename = filename
        
        self.zeilen=[]
        
        #Konfigurationsdatei öffnen und Zeilen lesen
        try:
            with open(self.filename, 'r') as fp:
                self.zeilen = fp.readlines()
        except:
            print('Fehler beim Bearbeiten der Datei', self.filename)
            #exit()
        
        #setzen von Großbuchstaben auf kleinbuchstaben
        for i in range(len(self.zeilen)):
            self.zeilen[i] = self.zeilen[i].lower()

    #Funktion zum ermitteln von dem gewählten Typ der zu plottenden Funktion 
    def getCheck(self):
            for z in self.zeilen:
                if z.startswith('check'):

                    z = z.replace('check', '')
                    z = z.replace(':', '')
                    z = z.strip()
                    z = z.replace(' ', '')
                    for s in self.funktionstype:
                        if s in z:
                            return s
                        
    #funktion zum ermitteln des passenden Dictionary zu dem Funktionstyp
    def select_funktionstyp(self,s):

        if s == 'messdaten':
            return self.messdaten_dict
        elif s == 'funktionsgleichung':
            return self.func_dict
        elif s == 'parametrisch':
            return self.param_func_dict
        elif s == 'mehredimensionalefunktion':
            return self.func_3D_dict
        elif s == 'uebertragungsfunktion':
            return self.func_ubertragung_dict


    #Hilfsfunktion zum Packen eines Paramater in der Dictionary
    def fill_key(self,dic, z):
        for k in dic.keys():
            if z.startswith(k):
                z1 = z.replace(k, '')
                z2 = z1.replace(':', '')
                z = z2.replace(' ', '')
                if 'label' in k:
                    dic[k] = z2.rstrip()

                    
                elif k == 'x_reihe' or k == 'y_reihe':
                    try:
                        z = z.replace(',', ' ')
                        dic[k] = [float(x) for x in z.split()]
                    except:
                        import error_message as em
                        app = em.App(k)
                        app.mainloop()    
                        
                elif k == 'grid' or k == 'legend':
                    z = z.replace('(ja/nein)', '')

                    if 'ja' in z:
                        dic[k] = True
                    else:
                        dic[k] = False

                elif ('linewidth' in k or 'a' == k or 'b' == k or 'step' in k or
                      ('start' in k or 'end' in k)):
                    try:
                        dic[k] = float(z)
                    except:
                        import error_message as em
                        app = em.App(k)
                        app.mainloop()




                else:
                    dic[k] = z.rstrip()

        return dic

    #fill_keys: füllt das passende Dictionary mit den gewählten Parameter aus der Konfig-Datei
    def fill_keys(self):
        global i
        s = self.getCheck()
        my_dict = self.select_funktionstyp(s)
        for i in range(len(self.zeilen)):
            if self.zeilen[i].startswith(s):
                break
        j = i + 2
        while not ('-----' in self.zeilen[j]):
            my_dict =self.fill_key(my_dict, self.zeilen[j])
            j += 1

        return my_dict


     

       	

