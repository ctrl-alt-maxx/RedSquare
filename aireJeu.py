#import vueMenu as menu
from cmath import rect
import tkinter as tk
from tkinter import BOTH, Canvas
#import os, sys, tkinter.filedialog
import c31Geometry2 as c31

root = tk.Tk()

# Couleur de fond 
root.config(background="LightSkyBlue1")

# Ajouter un titre à la fenêtre Tk
root.title("Jeu du carré rouge")

# Fixe la taille de la fenêtre en px
root.geometry("850x850")

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
rectWhite = c31.Rectangle(canvas, c31.Vecteur(450, 450), 850, 850, remplissage="yellow")
rectWhite.draw()

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


#carreRouge.bind("<B1-Motion>", glisser)

print("Rectangle1", c31.Rectangle.get_coordonnees(rectangle1))
print("rectwhite", c31.Rectangle.get_coordonnees(rectWhite))

if (carreRouge.coords)


root.mainloop()