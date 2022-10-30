
import tkinter as tk
from turtle import color
import c31Geometry2 as c31

root = tk.Tk()

# Couleur de fond
root.config(background="LightSkyBlue1")

# Ajouter un titre à la fenêtre TK
root.title("Jeu du carré rouge : Menu")

# Fixe la taille de la fenêtre en px
root.geometry("850x850")

# Texte pour afficher les consignes du jeu 
texteTitre = tk.Label(root, text="Jeu du carré rouge", background="white", foreground="black", padx=300, pady=300)
texteTitre.grid(column=10, row=11)


root.mainloop()