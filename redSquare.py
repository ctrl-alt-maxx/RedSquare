
from functools import partial
import tkinter as tk
from tkinter import Canvas, Label, Menu, Tk, ttk
from tkinter import messagebox
import c31Geometry2 as c31


root = tk.Tk()

# Pop-up window
#label = Label(root, text="Right-click anywhere to display a menu")
#label.pack(pady=40)
#popup = Menu(root, tearoff=0)
#popup.add_command(label="new")
#popup.add_command(label="edit")
#popup.add_separator()
#popup.add_command(label="save")

#def menu_popup(event):
#    try:
#        popup.tk_popup(event.x_root, event.y_root, 0)
#    finally:
#        popup.grab_release()

#root.bind("<ButtonPress-3>", menu_popup)
#button =ttk.Button(root, text="quit", command=root.destroy)



# Background color
root.config(background="royalblue")

# Ajouter un titre a la fenetre TK
root.title("Jeu du carré rouge")

# Fixe la taille de la fenetre en pixel
root.geometry("1000x1000")

menu  = tk.Label(root, text="Menu: Faites un choix:", background="white", foreground="black", padx="50", pady="100")

menu.grid(column=0, row=0)

# Bouton
def fooBouton(button):
   print("Votre choix: " + button)

buttonStart = tk.Button(root, text="start", command=fooBouton, width=8)
buttonStart.grid(column=1, row=0)

button = tk.Button(root, text="1. Facile", command=fooBouton, width=8)
button.grid(column=1, row=1)

button2 = tk.Button(root, text="2. Moyen", command=fooBouton, width=8)
button2.grid(column=1, row=2)

button3 = tk.Button(root, text="3. Difficile", command=fooBouton, width=8)
button3.grid(column=1, row=3)

buttonQuit = tk.Button(root, text="Quitter", command=fooBouton, width=8)
buttonQuit.grid(column=1, row=4)


#def hello():
 #   messagebox.showinfo("Choose a difficulty")

#b1 = tk.Button(root, text = "Start", command=hello)
#b1.pack()


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



