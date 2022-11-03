# ** COMPLETER **
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
import c31Geometry2 as c31
from functools import partial
from modeles import Rectangle
import csv
import datetime as dt

root = tk.Tk()

# Couleur de fond
root.config(background="LightSkyBlue1")

# Ajouter un titre à la fenêtre TK
root.title("Jeu du carré rouge : Menu")

# Fixe la taille de la fenêtre en px
root.geometry("850x850")

# Pour afficher les consignes 
L = tk.Label(root, text="Choississez un niveau de difficultés dans le menu.", width = 50, height = 20)
L.pack()

class VueMenu:
    def instruction():
        msg.showinfo(title="Instruction", message="Cliquez et maintenez le carré rouge le plus longtemps possible.")

    def menu():
        # Création d'un menuBar
        menubar = Menu(root)
        root.config(menu=menubar)

        # Creation du file_menu 
        file_menu = Menu(
            menubar,
            tearoff=0
        )

        # Ajouter des items dans le menu 
        file_menu.add_command(label='Facile', command=d.Facile)
        file_menu.add_command(label='Moyen', command=d.Moyen)
        file_menu.add_command(label='Difficle', command=d.Difficile)
        file_menu.add_separator()
        file_menu.add_command(label='Quitter', command=root.destroy)

        # Ajouter le file_menu au menuBar
        menubar.add_cascade(
            label="Menu",
            menu = file_menu
        )


class VueJeu:
    def canvasCreation():
        # Création du canvas 
        canvasBase = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")
        rectYellow = c31.Rectangle(canvasBase, c31.Vecteur(450, 450), 850, 850, remplissage="yellow")
        rectYellow.draw()

    def enregistrerScores():
        d = dt.datetime.now()
        # FICHIER CONTENANT LES TEMPS DES PARTIES PRÉCEDENTES
        f = open("wow.txt", "a")
        with f:
            fnames = ['Nom', 'Temps', 'Date Joué']
            csvwriter = csv.DictWriter(f, fieldnames=fnames)
            csvwriter.writerow( {'Nom' : name, 'Temps' : t, 'Date Joué' : d} ) 
        f.close()

    def montrerScores():
        # RÉPONSE POUR SI LA PERSONNE VEUT VOIR LES TEMPS PRÉCEDENTS
        answer = msg.askyesno("Question","Veux-tu voir le temps des autres parties?")

        if answer == True :
            score = tk.Tk()
            score.title('Tkinter Scores')
            score.resizable(True, False)
            score.geometry('800x400')
            
            col_names = ("Username", "Temps", "Date Joué")
            for i, col_name in enumerate(col_names, start=0):
                tk.Label(score, text=col_name).grid(row=0, column=i, padx=40)
                
            # ACCÈS AU FICHIER
            with open("wow.txt", "r", newline="\n") as scorefile:
                reader = csv.reader(scorefile)
                data = list(reader)
                
            scoreslist = []
            for i, row in enumerate(data):
                scoreslist.append(row[0])
                for col in range(0, 3):
                    tk.Label(score, text=row[col]).grid(row=i+1, column=col, padx=100)
                    
            score.mainloop()

instruction()

root.mainloop()

