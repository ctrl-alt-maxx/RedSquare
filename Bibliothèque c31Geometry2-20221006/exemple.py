
import tkinter as tk
from random import choice
from functools import partial
import c31Geometry2 as c31



root = tk.Tk()

# Background color
root.config(background="deep pink")

# Ajouter un titre a la fenetre TK
root.title("Ma premiere fenetre GUI")

# Fixe la taille de la fenetre en pixel
root.geometry("500x500")

texte = tk.Label(root, text="Hello World!", background="lawn green", foreground="deep sky blue", padx="50", pady="100")

texte.grid(column=0, row=0)

# Bouton 
def Foo():
    print("click")

button = tk.Button(root, text="Cliquez sur moi", command=Foo)
button.grid(column=1, row=1)

def ChangerRandom(label):
    couleur = "#"
    for i in range(0, 6) :
        couleur += choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"])
    
    label.config(background=couleur)

btn2 = tk.Button(root, text="Changer la couleur", command=partial(ChangerRandom, texte))

btn2.grid(column=2, row=1)

# Change le texte 
text_champ = tk.StringVar(root)
champ = tk.Entry(root, textvariable=text_champ)
champ.grid(column=0, row=1)

def lecture(strvar):
    print(strvar.get())

btn3 = tk.Button(root, text="Afficher message", command=partial(lecture, text_champ))
btn3.grid(column=3, row=3)

def log(var, e):
    print(var)

# Evenement 
root.bind("<KeyPress-q>", partial(print, "allo"))
root.bind("<ButtonPress-3>", partial(print, "allo"))
root.bind("<Control-KeyRelease-q>", exit)
root.bind("<Double-ButtonPress-3>", exit)
# ButtonPress-3 is a right click 

# Canvas 
canvas = tk.Canvas(root, background="white")

canvas.create_line((10, 10), (200, 10), fill="blue")
canvas.create_line((10, 10), (10, 200), fill="green")
canvas.create_line((10, 10), (141, 141), fill="red")

canvas.create_rectangle((150, 150), (180, 225), fill="yellow", outline="salmon")

canvas.grid(column=0, row=2)

carre = c31.Carre(canvas, c31.Vecteur(50, 50), 100, remplissage="magenta2")
carre.draw()


loop = c31.LoopEvent(root, partial(log, "Cliquez-Loop", None), 1000)
loop.start()

def mvt(forme):
    forme.translate(c31.Vecteur(4, 0))
    forme.draw()

loop2 = c31.LoopEvent(canvas, partial(mvt, carre))
loop2.start()






# Creer des widgets, il faut le stocker dans une variable dans un Tk dans un dossier parent,
# et tous les autres parametres sont les noms, etc. mais en chaines de caracteres, donc,
# widget = Tk.Widget(root,...,p="v",...)

# Lui donner de la couleur 
# widget.config(p="v")

# Si on veut la valeur du parametre (mettre le nom du parametre en crochet)
# widget.cget("p")

# Pour placer des objets 
# widget.pack() 

# Autre maniere de le placer  (en x et y en pixel pres [width, height])
# Avec "place", on peut trouver les coordonees relatives 
# widget.place(x=0, y=0)

# widget.grid(column; row)     -> donne sa colonne et sa ligne 



root.mainloop()

