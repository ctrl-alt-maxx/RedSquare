import random
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
import c31Geometry2 as c31
import csv
import datetime as dt
from controlleurs import MenuController
from modeles import Mouvement


class VueMenu:

    # AFFICHAGE DES CONSIGNES 
    def instruction():
        msg.showinfo(title="Instruction", message="Cliquez et maintenez le carré rouge le plus longtemps possible.")

    instruction()

    def menu():
        # CRÉATION D'UN MENUBAR
        menubar = Menu(VueMenu.root)
        VueMenu.root.config(menu=menubar)

        # CRÉATION DU FILE_MENU
        file_menu = Menu(
            menubar,
            tearoff=0
        )

        # AJOUTER DES ITEMS DANS LE MENU
        file_menu.add_command(label='Facile', command=MenuController.d.Facile)
        file_menu.add_command(label='Moyen', command=MenuController.d.Moyen)
        file_menu.add_command(label='Difficle', command=MenuController.d.Difficile)
        file_menu.add_separator()
        file_menu.add_command(label='Quitter', command=VueMenu.root.destroy)

        # AJOUTER LE FILE_MENU AU MENUBAR
        menubar.add_cascade(
            label="Menu",
            menu = file_menu
        )


class Difficulté:

    # PLUS LA VALEUR EST PETIT, PLUS LE MOUVEMENT EST DOUX
    defaultSpeed = 0 
    def Facile(self):
        self.defaultSpeed = 1000
        
        Mouvement.loop1, self.defaultSpeed
        Mouvement.loop2, self.defaultSpeed
        Mouvement.loop3, self.defaultSpeed
        Mouvement.loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()

    def Moyen(self):
        self.defaultSpeed = 200

        Mouvement.loop1, self.defaultSpeed
        Mouvement.loop2, self.defaultSpeed
        Mouvement.loop3, self.defaultSpeed
        Mouvement.loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()
            
    def Difficile(self):
        self.defaultSpeed = 50

        Mouvement.loop1, self.defaultSpeed
        Mouvement.loop2, self.defaultSpeed
        Mouvement.loop3, self.defaultSpeed
        Mouvement.loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()
        

d = Difficulté()

class VueJeu:

    # CRÉATION DU CANVAS
    def canvasCreation():
        canvasBase = tk.Canvas(VueMenu.root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")
        rectYellow = c31.Rectangle(canvasBase, c31.Vecteur(450, 450), 850, 850, remplissage="yellow")
        rectYellow.draw()

        canvasBase.pack()

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



VueMenu.root.mainloop()

