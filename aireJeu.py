#import vueMenu as menu
from cmath import rect
from functools import partial
from math import dist
import tkinter as tk
from tkinter import BOTH, Canvas, StringVar, Variable
#import os, sys, tkinter.filedialog
import c31Geometry2 as c31
from tkinter import Menu

root = tk.Tk()

# Couleur de fond 
root.config(background="LightSkyBlue1")

# Ajouter un titre à la fenêtre Tk
root.title("Jeu du carré rouge")

# Fixe la taille de la fenêtre en px
root.geometry("850x850")


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

# Avoir un fichier excutable 
#pyExec = sys.executable

# En cliquant sur une option, une nouvelle fenêtre s'affiche
#def open():
#    if (menu.file_menu != "Quitter") :
#        print("not quit")
#        PathPyFile = tkinter.filedialog.askopenfilename(title="Open a file",filetypes=[('vueMenu','.py')])
#        os.system('%s %s' % (pyExec, PathPyFile))

#open()

# Création du canvas 
canvas = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")
rectYellow = c31.Rectangle(canvas, c31.Vecteur(450, 450), 850, 850, remplissage="yellow")
rectYellow.draw()

# Création des rectangles
# 1. Rectangle bleu gauche
rectangle1 = c31.Rectangle(canvas, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
rectangle1.draw()

# 2. Rectangle bleu superieur droit
rectangle2 = c31.Rectangle(canvas, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
rectangle2.draw()

# 3. Rectangle bleu inferieur gauche 
rectangle3 = c31.Rectangle(canvas, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
rectangle3.draw()

# 4. Rectangle bleu infereieur droit 
rectangle4 = c31.Rectangle(canvas, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
rectangle4.draw()

canvas.pack()

# Création du carré rouge 
carreRouge = Canvas(root, width=40, height=40, background="red")
carreRouge.place(x=420, y=250, anchor=tk.CENTER)

# Fonction pour glisser (drag) carré rouge 
def glisser(event) :
    event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)


carreRouge.bind("<B1-Motion>", glisser)

print("Rectangle1", c31.Rectangle.get_coordonnees(rectangle1))
print("rectJaune", c31.Rectangle.get_coordonnees(rectYellow))

#carre = c31.Carre(canvas, c31.Vecteur(270, 249), 40, remplissage="green")
#carre.draw()

#carre.bind("<B1-Motion>", glisser)

#print("Carre", c31.Carre.get_coordonnees(carre))
#print("CarreRougeCanvas", canvas.coords(carreRouge))

#def move() :
#    while (carreRouge.bind("<B1-Motion>", glisser)) :
#        if (carreRouge.place(x=879)) :
#            print("out")

#var = StringVar()
#def outsideYellowRect(event) :
#    var.set("is outside")

def mvt(forme) :
    forme.translate(c31.Vecteur(10,0)) 
    forme.draw()

def mvtBack(forme) :
    forme.translate(c31.Vecteur(8,0))
    forme.translate(c31.Vecteur(0,9))
    forme.draw()



loop = c31.LoopEvent(canvas, partial(mvt, rectangle1))
loop.start()

def mouseDragged() :
    root.bind("<B1-Motion>", partial(print, "dragged"))
    carreRouge.bind("<B1-Motion>", glisser)

mouseDragged()

root.mainloop()