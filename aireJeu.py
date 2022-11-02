#import vueMenu as menu
from cmath import rect
from email import message
from functools import partial
import tkinter as tk
from tkinter import BOTH, Canvas, Message, StringVar, TclError, Variable
from tkinter import dialog
from turtle import distance
#import os, sys, tkinter.filedialog
import c31Geometry2 as c31
from tkinter import Menu
from tkinter import messagebox as msg

root = tk.Tk()

# Couleur de fond 
root.config(background="LightSkyBlue1")

# Ajouter un titre à la fenêtre Tk
root.title("Jeu du carré rouge")

# Fixe la taille de la fenêtre en px
root.geometry("850x850")

# DETERMINE LA VITTESE DES FORMES BLEUES AU DÉBUT DU JEU
class Difficulté:
    defaultSpeed = 0 # THE LOWER THE VALUE, THE CLEANNER THE MOVEMENT WITH FASTER SPEED
    def Facile(self):
        self.defaultSpeed = 1000
       
        loop1 = c31.LoopEvent(canvasBase, partial(mvt1, Rectangle.rectangle1), self.defaultSpeed)
        loop2 = c31.LoopEvent(canvasBase, partial(mvt2, Rectangle.rectangle2), self.defaultSpeed)
        loop3 = c31.LoopEvent(canvasBase, partial(mvt3, Rectangle.rectangle3), self.defaultSpeed)
        loop4 = c31.LoopEvent(canvasBase, partial(mvt4, Rectangle.rectangle4), self.defaultSpeed)

        loop1.start()
        loop1.start()
        loop2.start()
        loop3.start()
        loop4.start()

    def Moyen(self):
        self.defaultSpeed = 200

        loop1 = c31.LoopEvent(canvasBase, partial(mvt1, Rectangle.rectangle1), self.defaultSpeed)
        loop2 = c31.LoopEvent(canvasBase, partial(mvt2, Rectangle.rectangle2), self.defaultSpeed)
        loop3 = c31.LoopEvent(canvasBase, partial(mvt3, Rectangle.rectangle3), self.defaultSpeed)
        loop4 = c31.LoopEvent(canvasBase, partial(mvt4, Rectangle.rectangle4), self.defaultSpeed)

        loop1.start()
        loop2.start()
        loop3.start()
        loop4.start()
        
    def Difficile(self):
        self.defaultSpeed = 50

        loop1 = c31.LoopEvent(canvasBase, partial(mvt1, Rectangle.rectangle1), self.defaultSpeed)
        loop2 = c31.LoopEvent(canvasBase, partial(mvt2, Rectangle.rectangle2), self.defaultSpeed)
        loop3 = c31.LoopEvent(canvasBase, partial(mvt3, Rectangle.rectangle3), self.defaultSpeed)
        loop4 = c31.LoopEvent(canvasBase, partial(mvt4, Rectangle.rectangle4), self.defaultSpeed)

        loop1.start()
        loop2.start()
        loop3.start()
        loop4.start()
      
d = Difficulté()


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
canvasBase = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")
#rectYellow = c31.Rectangle(canvasBase, c31.Vecteur(450, 450), 850, 850, remplissage="yellow")
#rectYellow.draw()

class Rectangle:
    # Création des rectangles
    # 1. Rectangle bleu gauche
    rectangle1 = c31.Rectangle(canvasBase, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
    rectangle1.draw()

    # 2. Rectangle bleu superieur droit
    rectangle2 = c31.Rectangle(canvasBase, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
    rectangle2.draw()

    # 3. Rectangle bleu inferieur gauche 
    rectangle3 = c31.Rectangle(canvasBase, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
    rectangle3.draw()

    # 4. Rectangle bleu infereieur droit 
    rectangle4 = c31.Rectangle(canvasBase, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
    rectangle4.draw()


canvasBase.pack()

# Création du carré rouge 
carreRouge = Canvas(root, width=40, height=40, background="red")
carreRouge.place(x=420, y=250, anchor=tk.CENTER)

# Fonction pour glisser (drag) carré rouge 
def glisser(event) :
    event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)

carreRouge.bind("<B1-Motion>", glisser)

carre = c31.Carre(canvasBase, c31.Vecteur(270, 249), 40, remplissage="green")
carre.draw()

def mvt1(forme) :
    forme.translate(c31.Vecteur(10,0)) 
    forme.translate(c31.Vecteur(0,10)) 
    forme.draw()

def mvt2(forme) :
    forme.translate(c31.Vecteur(0,10)) 
    forme.translate(c31.Vecteur(0,10)) 
    forme.draw()

def mvt3(forme) :
    forme.translate(c31.Vecteur(10,0)) 
    forme.translate(c31.Vecteur(10,0)) 
    forme.draw()

def mvt4(forme):
    forme.translate(c31.Vecteur(0,-8)) 
    forme.translate(c31.Vecteur(-8,0)) 
    forme.draw()

def mvtBack(forme) :
    forme.translate(c31.Vecteur(0,8))
    forme.translate(c31.Vecteur(8,0))
    forme.draw()


loop1 = c31.LoopEvent(canvasBase, partial(mvt1, Rectangle.rectangle1))
loop2 = c31.LoopEvent(canvasBase, partial(mvt2, Rectangle.rectangle2))
loop3 = c31.LoopEvent(canvasBase, partial(mvt3, Rectangle.rectangle3))
loop4 = c31.LoopEvent(canvasBase, partial(mvt4, Rectangle.rectangle4))

loop1.start()
loop2.start()
loop3.start()
loop4.start()


go = bool(True)


##def update():
 #   Rectangle.rectangle2.draw()

#if rectangle2.get_position() == c31.Vecteur(300,95) :
#    go = bool(False)
    
#if go == bool(True) : 
#    loop.start()

#e = c31.LoopEvent(root, update, d.defaultSpeed)
#e.startImmediately()

# CACHE LE CURSEUR SUR LE CARREÉ ROUGE
carreRouge.config(cursor="none")

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

carreRouge.bind('<B1-Motion>', glisser)

print("Rectangle1", c31.Rectangle.get_coordonnees(Rectangle.rectangle1))
print("Rectangle2", c31.Rectangle.get_coordonnees(Rectangle.rectangle2))
print("Rectangle3", c31.Rectangle.get_coordonnees(Rectangle.rectangle3))
print("Rectangle4", c31.Rectangle.get_coordonnees(Rectangle.rectangle4))
#print("rectJaune", c31.Rectangle.get_coordonnees(rectYellow))


def toucheEnemie():
    if (carreRouge.get_event.x) :
        print

x = canvasBase.winfo_pointerx()
y = canvasBase.winfo_pointery()
abs_coord_x = canvasBase.winfo_pointerx() - canvasBase.winfo_rootx()
abs_coord_y = canvasBase.winfo_pointery() - canvasBase.winfo_rooty()
print("x", x)
print("y", y)
print("abs_coord_x", abs_coord_x)
print("abs_coord_y", abs_coord_y)

def get_absolute_position(event):
    x = event.x
    y = event.y
    return x, y

def endGame():
    msg.showerror(title="error", message="end of game", master=root).show()

def counter():
    whenToStop = 5000
    #root.after(whenToStop, root.destroy)
    endGame()

counter()
root.mainloop()