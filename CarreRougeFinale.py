from functools import partial
from tkinter import Canvas
import tkinter as tk
import c31Geometry2 as c31
import random
from tkinter import messagebox as msg
import csv
import datetime as dt


root = tk.Tk()

# COULEUR DE FOND
root.config(background="LightSkyBlue1")

# AJOUTER UN TITRE À LA FENÊTRE TKINTER
root.title("Jeu du carré rouge")

# FIXDE LA TAILLE EN PIXEL
root.geometry("850x850")

class Difficulte() :
    # PLUS LA VALEUR EST PETIT, PLUS LE MOUVEMENT EST DOUX
    defaultSpeed = 0 
    def Facile(self):
        self.defaultSpeed = 1000
        
        loop1, self.defaultSpeed
        loop2, self.defaultSpeed
        loop3, self.defaultSpeed
        loop4, self.defaultSpeed


    def Moyen(self):
        self.defaultSpeed = 200

        loop1, self.defaultSpeed
        loop2, self.defaultSpeed
        loop3, self.defaultSpeed
        loop4, self.defaultSpeed
            
    def Difficile(self):
        self.defaultSpeed = 50

        loop1, self.defaultSpeed
        loop2, self.defaultSpeed
        loop3, self.defaultSpeed
        loop4, self.defaultSpeed

d = Difficulte()

# CRÉATION D'UN MENUBAR
menubar = tk.Menu(root)
root.config(menu=menubar)

# CRÉATION DU FILE_MENU
file_menu = tk.Menu(
    menubar,
    tearoff=0
)

# AJOUTER DES ITEMS DANS LE MENU
file_menu.add_command(label='Facile', command=d.Facile)
file_menu.add_command(label='Moyen', command=d.Moyen)
file_menu.add_command(label='Difficle', command=d.Difficile)
file_menu.add_separator()
file_menu.add_command(label='Quitter', command=root.destroy)

# AJOUTER LE FILE_MENU AU MENUBAR
menubar.add_cascade(
    label="Menu",
    menu = file_menu
)

#CRÉATION DU CANVAS
canvasBase = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black") 
canvasBase.pack()

# CRÉATION DES RECTANGLES/ENEMIES 
# 1. RECTANGLE BLEU GAUCHE
en1 = c31.Rectangle(canvasBase, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
en1.draw()

# 2. RECTANGLE BLEU SUPÉRIUR DROIT
en2 = c31.Rectangle(canvasBase, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
en2.draw()

# 3. RECTANGLE BLEU INFÉRIEUR GAUCHE 
en3 = c31.Rectangle(canvasBase, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
en3.draw()

# 4. RECTANGLE BLEU INFÉRIEUR DROIT 
en4 = c31.Rectangle(canvasBase, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
en4.draw()


# CRÉATION DU CARRÉ ROUGE 
carreRouge = tk.Canvas(root, width=40, height=40, background="red")
carreRouge.place(x=420, y=250, anchor=tk.CENTER)

# CACHE LE CURSEUR SUR LE CARREÉ ROUGE
carreRouge.config(cursor="none")

# FONCTION POUR TRAÎNER (drag) LE CARRÉ ROUGE 
def trainer(event) :
    event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)

carreRouge.bind("<B1-Motion>", trainer)

# AFFICHAGE DES CONSIGNES 
def instruction():
    msg.showinfo(title="Instruction", message="Cliquez et maintenez le carré rouge le plus longtemps possible.")

instruction()
    

# CHAQUE ENEMIE À SON PROPRE MOUVEMENT (le sens de direction)
def mvt1(forme): 
    forme.translate(c31.Vecteur(2,0)) 
    forme.translate(c31.Vecteur(0,2)) 
    en1.draw()
                
def mvt2(forme): 
    forme.translate(c31.Vecteur(0,2)) 
    forme.translate(c31.Vecteur(0,2)) 
    en2.draw()

def mvt3(forme): 
    forme.translate(c31.Vecteur(10,0)) 
    forme.translate(c31.Vecteur(10,0)) 
    en3.draw()
                
def mvt4(forme): 
    forme.translate(c31.Vecteur(0,-8)) 
    forme.translate(c31.Vecteur(-8,0)) 
    en4.draw() 

# EXÉCUTE APRÈS UN CERTAIN TEMPS

loop1 = c31.LoopEvent(canvasBase, partial(mvt1, en1)) 
loop1.start()

loop2 = c31.LoopEvent(canvasBase, partial(mvt2, en2))
loop2.start()

loop3 = c31.LoopEvent(canvasBase, partial(mvt3, en3))
loop3.start()
            
loop4 = c31.LoopEvent(canvasBase, partial(mvt4, en4))
loop4.start()

def enregistrerScores():
    d = dt.datetime.now()
    t = random.randrange(1, 21)
    name = "Marc"

    # FICHIER CONTENANT LES TEMPS DES PARTIES PRÉCEDENTES
    f = open("scores.csv", "a")
    with f:
        fnames = ['Nom', 'Temps', 'Date Joué']
        csvwriter = csv.DictWriter(f, fieldnames=fnames)
        csvwriter.writerow( {'Nom' : name, 'Temps' : t, 'Date Joué' : d} ) 
    f.close()

def montrerScores():
    # RÉPONSE POUR SI L'UTILISATEUR VEUT VOIR LES TEMPS PRÉCEDENTS
    reponse = msg.askyesno("Question","Voulez-vous voir le temps des parties précédentes?")

    if reponse == True :
        score = tk.Tk()
        score.title('Tkinter Scores')
        score.geometry('800x400')
            
        col_noms = ("Username", "Temps", "Date Joué")
        for i, col_name in enumerate(col_noms, start=0):
            tk.Label(score, text=col_name).grid(row=0, column=i, padx=40)
                
        # ACCÈS AU FICHIER
        with open("scores.csv", "r", newline="\n") as scorefile:
            reader = csv.reader(scorefile)
            data = list(reader)
                
        scoresliste = []
        for i, row in enumerate(data):
            scoresliste.append(row[0])
            for col in range(0, 3):
                tk.Label(score, text=row[col]).grid(row=i+1, column=col, padx=100)
                    
        score.mainloop()
    
# PERMET DE DÉTRUIRE LE WINDOW ROOT 
root.after(3099, root.destroy)

root.mainloop()

    

    