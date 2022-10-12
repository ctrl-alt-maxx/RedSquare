import tkinter as tk
from turtle import Vec2D, back
import c31Geometry2 as geo
import math

def rotation():
    ligne.rotate_mat(R)
    rectangle.rotate_mat(R)
    carre.rotate_mat(R)
    croix.rotate_mat(R)
    ligne_dash.rotate_mat(R)
    cercle.rotate_mat(R)
    oval.rotate_mat(R)
    update()
    
def agrandir():
    ligne.resize(2)
    rectangle.resize(2)
    carre.resize(2)
    croix.resize(2)
    ligne_dash.resize(2)
    cercle.resize(2)
    oval.resize(2)
    
def reduire():
    ligne.resize(0.5)
    rectangle.resize(0.5)
    carre.resize(0.5)
    croix.resize(0.5)
    ligne_dash.resize(0.5)
    cercle.resize(0.5)
    oval.resize(0.5)
    
def gauche():
    ligne.translate(geo.Vecteur.gauche() * 10)
    rectangle.translate(geo.Vecteur.gauche() * 10)
    carre.translate(geo.Vecteur.gauche() * 10)
    croix.translate(geo.Vecteur.gauche() * 10)
    ligne_dash.translate(geo.Vecteur.gauche() * 10)
    cercle.translate(geo.Vecteur.gauche() * 10)
    oval.translate(geo.Vecteur.gauche() * 10)
    
def droite():
    ligne.translate(geo.Vecteur.droite() * 10)
    rectangle.translate(geo.Vecteur.droite() * 10)
    carre.translate(geo.Vecteur.droite() * 10)
    croix.translate(geo.Vecteur.droite() * 10)
    ligne_dash.translate(geo.Vecteur.droite() * 10)
    cercle.translate(geo.Vecteur.droite() * 10)
    oval.translate(geo.Vecteur.droite() * 10)

def update():
    l1.draw()
    l2.draw()
    ligne.draw()
    rectangle.draw()
    carre.draw()
    croix.draw()
    ligne_dash.draw()
    cercle.draw()
    oval.draw()

if __name__ == "__main__" :
    R = geo.Rotation(-1.047)
    Bary = geo.Vecteur.zero()
    
    root = tk.Tk()
    root.title("Test de geometry")
    root.geometry("500x350")
    
    button = tk.Button(root, text="Rotation de pi/3", command=rotation)
    button.grid(column=0, row=0)
    button2 = tk.Button(root, text="Agrandir", command=agrandir)
    button2.grid(column=0, row=1)
    button3 = tk.Button(root, text="Réduire", command=reduire)
    button3.grid(column=1, row=1)
    button4 = tk.Button(root, text="Déplacer vers la gauche", command=gauche)
    button4.grid(column=0, row=2)
    button4 = tk.Button(root, text="Déplacer vers la gauche", command=droite)
    button4.grid(column=1, row=2)
    
    canvas = tk.Canvas(root, background='white')
    canvas.grid()
    
    l1 = geo.Ligne(canvas, geo.Vecteur(125, 75), 100, math.pi / 2, epaisseur=5)
    l2 = geo.Ligne(canvas, geo.Vecteur(175, 125), 100, 0, epaisseur=5)
    
    ligne = geo.Ligne(canvas, geo.Vecteur(50, 125), 50, 0, bordure="red", epaisseur=10)
    rectangle = geo.Rectangle(canvas, geo.Vecteur(150, 125), 100, 50, 0, remplissage="blue")
    carre = geo.Carre(canvas, geo.Vecteur(50, 200), 50, remplissage="yellow")    
    croix = geo.Croix(canvas, geo.Vecteur(150, 200), 25, 50, bordure="#909", epaisseur=5)
    ligne_dash = geo.Ligne(canvas, geo.Vecteur(200, 200), 50, 0, bordure="green", dash=geo.Dash(3, 3), epaisseur=5)
    cercle = geo.Cercle(canvas,  geo.Vecteur(50, 50), 25, remplissage="gray")
    oval = geo.Oval(canvas,  geo.Vecteur(150, 50), 25, 50, remplissage="gray")
    
    update()
    
    #e = geo.LoopEvent(root, update, 100)
    #e.startImmediately() 
    root.mainloop()