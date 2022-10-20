from functools import partial
import tkinter as tk
from tkinter import CENTER, Canvas, Label, Menu
import c31Geometry2 as c31

go = bool(True)
root = tk.Tk()
# RAPPROCHE LE CURSEUR DU CARRÉ
root.state('zoomed')

# Background color
root.config(background="royalblue")

# Ajouter un titre a la fenetre TK
root.title("Jeu du carré rouge")

# Fixe la taille de la fenetre en pixel
root.geometry("1000x1000")


# Creating canvas 
canvas = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")

# DETERMINE LA VITTESE DES FORMES BLEUES AU DÉBUT DU JEU
class Difficulté:
    defaultSpeed = 2000
    def Facile(self):
        self.defaultSpeed = 1000
        self.color = "red"
        loop = c31.LoopEvent(canvas,partial(mvt,rectangle2), self.defaultSpeed)
        loop.start()

    def Moyen(self):
        self.defaultSpeed = 500
        loop = c31.LoopEvent(canvas,partial(mvt,rectangle2), self.defaultSpeed)
        loop.start()
        
    def Difficile(self):
        self.defaultSpeed = 100
        loop = c31.LoopEvent(canvas,partial(mvt,rectangle2), self.defaultSpeed)
        loop.start()
      
d = Difficulté()

#canvas = c31.Carre(root, c31.Vecteur(450,450), 450, bordure="black", remplissage="white", epaisseur=50)

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

canvas.pack()

def log(var, e):
    print(var)


#carre = c31.Carre(canvas, c31.Vecteur(225, 225), 40, remplissage="red")
#carre.draw()

# loop = c31.LoopEvent(root, partial(log, "Cliquez-Loop", None), 1000)
# loop.start()

def mvt(forme):
    forme.translate(c31.Vecteur(4, 0))
    #forme.translateTo(c31.Vecteur(4,0), c31.Vecteur(5,10))
    forme.draw()
    forme.translate(c31.Vecteur(5, 10))
    
# Mouvement du carree rouge on its own
#loop2 = c31.LoopEvent(canvas, partial(mvt, carre))
#loop2.start()

def log(var, e):
    print(var)


loop = c31.LoopEvent(root, partial(log, "Cliquez-loop", None), 1000)
loop.start()

# POP_UP - RIGHT-CLICK

label = Label(root)
label.pack()

# Ajout du menu
popup = Menu(root, tearoff=0)

# Adding items to the menu 
popup.add_command(label="Facile", command=d.Facile)
popup.add_command(label="Moyen", command=d.Moyen)
popup.add_command(label="Difficile", command=d.Difficile)
popup.add_separator()
popup.add_command(label="Quitter", command=root.destroy)

def menu_popup(event):
    # Affichage du pop-up menu
    try:
        popup.tk_popup(event.x_root, event.y_root)
    finally:
        # Release the grab
        popup.grab_release()

# Button 2 for MAC, buttonPress-3 for windows 
root.bind("<ButtonPress-3>", menu_popup)
root.bind(canvas, "<ButtonPress-1>", partial(print, "allo"))
root.bind("<ButtonPress-1>", partial(print, "pressed"))
root.bind("<ButtonRelease>", partial(print, "released"))
root.bind("<B1-Motion>", partial(print, "dragged"))

def mvt(forme): forme.translateTo(c31.Vecteur(300,95))

def update():
    rectangle2.draw()

# loop = c31.LoopEvent(canvas,partial(mvt,rectangle2), 300)

if rectangle2.get_position() == c31.Vecteur(300,95) :
    go = bool(False)
    
if go == bool(True) : 
    loop.start()
    
e = c31.LoopEvent(root, update, d.defaultSpeed)
e.startImmediately()

def drag(event) :
    event.widget.place(x=event.x_root, y=event.y_root, anchor=CENTER)

carre2 = Canvas(root, width=40, height=40, bg="red")
carre2.place(x=225, y=225, anchor=CENTER)
carre2.bind("<B1-Motion>", drag)

# CACHE LE CURSEUR SUR LE CARREÉ ROUGE
carre2.config(cursor="none")
root.mainloop()
