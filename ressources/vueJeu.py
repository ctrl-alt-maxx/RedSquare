from functools import partial
import aireJeu as jeu
import tkinter as tk
from tkinter import CENTER, Canvas
import c31Geometry2 as c31

def glisser(event) :
    event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)


#carre = c31.Carre(tk.Canvas, c31.Vecteur(225, 225), 40, remplissage="red")
#carre.draw()

carre2 = tk.Canvas(jeu.root, width=40, height=40, bg="red")
carre2.place(x=225, y=225, anchor=CENTER)

carre2.bind("<B1-Motion>", glisser)
