# ** COMPLETER **
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
import c31Geometry2 as c31
from functools import partial
from modeles import Rectangle

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


instruction()

root.mainloop()

