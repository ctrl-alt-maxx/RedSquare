import tkinter as tk
from tkinter import *
import c31Geometry2 as c31

root = tk.Tk()
root.geometry("500x500")


c = tk.Canvas(root, width=450, height=450)

geo = c31.Carre(c, c31.Vecteur(100, 100), 40, remplissage="black")
geo.draw()

root.mainloop()