from functools import partial
import tkinter as tk
from tkinter import Canvas, Label, Menu, Tk, ttk
from turtle import width
import c31Geometry2 as c31



root = tk.Tk()

# Background color
root.config(background="royalblue")

# Ajouter un titre a la fenetre TK
root.title("Jeu du carré rouge")

# Fixe la taille de la fenetre en pixel
root.geometry("1000x1000")



# Bouton
def fooBouton(button):
   print("Votre choix: " + button)


button = tk.Button(root, text="1. Facile", command=fooBouton, width=8)
button.grid(column=1, row=1)

button2 = tk.Button(root, text="2. Moyen", command=fooBouton, width=8)
button2.grid(column=1, row=2)

button3 = tk.Button(root, text="3. Difficile", command=fooBouton, width=8)
button3.grid(column=1, row=3)

buttonQuit = tk.Button(root, text="Quitter", command=fooBouton, width=8)
buttonQuit.grid(column=1, row=4)



# Creating canvas 
canvas = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")




# Creating rectangles
# 1. rectangle bleu gauche
rectangle1 = c31.Rectangle(canvas, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
rectangle1.draw()


# 2. rectangle bleu superieur droit
rectangle2 = c31.Rectangle(canvas, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
rectangle2.draw()

# 3. rectangle bleu inferieur gauche 
rectangle3 = c31.Rectangle(canvas, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
rectangle3.draw()

# 4. rectangle bleu infereieur droit 
rectangle4 = c31.Rectangle(canvas, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
rectangle4.draw()

canvas.grid(column=0, row=0)



carre = c31.Carre(canvas, c31.Vecteur(225, 225), 40, remplissage="red")
carre.draw()