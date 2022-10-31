# ** COMPLETER **
import tkinter as tk
from tkinter import Menu

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

# Création d'un menuBar
menubar = Menu(root)
root.config(menu=menubar)

# Creation du file_menu 
file_menu = Menu(
    menubar,
    tearoff=0
)

# Ajouter des items dans le menu 
file_menu.add_command(label='Facile')
file_menu.add_command(label='Moyen')
file_menu.add_command(label='Difficle')
file_menu.add_separator()
file_menu.add_command(label='Quitter', command=root.destroy)

# Ajouter le file_menu au menuBar
menubar.add_cascade(
    label="Menu",
    menu = file_menu
)

root.mainloop()

