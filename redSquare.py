
from functools import partial
import tkinter as tk
from tkinter import Canvas, Label, Menu, Tk, ttk
from turtle import width
import c31Geometry2 as c31

go = bool(True)
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

# startscreen = c31.Carre(canvas, c31.Vecteur(225,225),600,remplissage="pink")
# # startscreen.draw()

# def hide_me(event):
#     event.widget.grid_forget()

# def callback(Buttons):
#    Buttons.bind('<Button>', hide_me)


# def callback_and_hide(button):
#     callback(Play_Button1)
#     button.grid_forget()

# Play_Button1 = Button(master = window,text='ㅤㅤ',command=lambda: callback_and_hide(Play_Button1))
# Play_Button1.config(bg="white",fg="black")
# Play_Button1.place(x=54, y=157, width=61, height=61)
    

# def Start():
#    startscreen.resize(0)
#    startscreen.draw()
#    buttonStart.widget.grid_remove()
   
# buttonStart = tk.Button(root,text="Start",command=Start)
# buttonStart.grid(column=0, row=0)





# VVVVVV CAN MODIFY FROM THIS POINT VVVVVV
  
def mvt(forme): 
    forme.translateTo(c31.Vecteur(300,200))
    #rectangle2.origine = c31.Vecteur(300,200)
    if():
        
  


def update():
    rectangle2.draw()
   
    loop.start()  

    
loop = c31.LoopEvent(canvas,partial(mvt,rectangle2),100)    
  
  
     
# if rectangle2.get_position() == c31.Vecteur(300,95) :
#     go = bool(False)
    
# if go == bool(True) : 
   
    
e = c31.LoopEvent(root, update, 100)
e.startImmediately()  


root.mainloop()



