import tkinter as tk 
from tkinter import  *
import c31Geometry2 as geo

root = tk.Tk()
root.geometry("600x600") # width and height


def mouvementCarre(event):
     l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
     # carre('<B1-Motion>')
     # root.bind(, carre)
     
     c = tk.Canvas(root, width=450, height=450, background="green")
     # c.grid()
     c.pack()
     g = geo.Carre(c, geo.Vecteur(int(event.x), int(event.y)), 50, remplissage="black") # c31.Vecteur(int(event.x), int(event.y))
     g.draw()
     geo.Vecteur.get_coordonnee(g)
     # c31.LoopEvent(root, callback= lambda : carre)    


def carre(event):
     c = tk.Canvas(root, width=450, height=450, background="green")
     # c.pack()
     carre = geo.Carre(c, geo.Vecteur(int(event.x), int(event.y)), 50, remplissage="black")
     carre.draw()  


root.title("Mouvement du carre rouge")
l1 = tk.Label(root, text='to Display',bg='yellow',font=30)
l1.pack(padx=30,pady=30)
# c = tk.Canvas(root, width=450, height=450, background="green")
# c.grid()
# c.pack()
# c31 = c31.Carre(c, c31.Vecteur(100, 100), 70, remplissage="black")
# c31.draw()    
root.bind('<B1-Motion>', mouvementCarre)

root.mainloop()