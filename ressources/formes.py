from functools import partial
import c31Geometry2 as c31
import tkinter as tk

root = tk.Tk()
root.config(background="royalblue")
root.title("Jeu du carre rouge")
root.geometry("1000x1000")


# Creating canvas 
canvas = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")


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

canvas.grid(column=0, row=0)

def log(var, e):
    print(var)


carre = c31.Carre(canvas, c31.Vecteur(225, 225), 40, remplissage="red")
carre.draw()

loop = c31.LoopEvent(root, partial(log, "Cliquez-Loop", None), 1000)
loop.start()

def mvt(forme):
    forme.translate(c31.Vecteur(4, 0))
    #forme.translateTo(c31.Vecteur(4,0), c31.Vecteur(5,10))
    forme.draw()
    forme.translate(c31.Vecteur(5, 10))
    

loop2 = c31.LoopEvent(canvas, partial(mvt, carre))
loop2.start()

def log(var, e):
    print(var)


loop = c31.LoopEvent(root, partial(log, "Cliquez-loop", None), 1000)
loop.start()

root.mainloop()