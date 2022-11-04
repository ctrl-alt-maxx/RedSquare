from functools import partial
from tkinter import Canvas
import tkinter as tk
import c31Geometry2 as c31
from vues import VueJeu, VueMenu

class Rectangle :

    # CRÉATION DES RECTANGLES/ENEMIES
    
    def enemie() : 
        # 1. RECTANGLE BLEU GAUCHE
        en1 = c31.Rectangle(VueJeu.canvasBase, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
        en1.draw()

        # 2. RECTANGLE BLEU SUPÉRIUR DROIT
        en2 = c31.Rectangle(VueJeu.canvasBase, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
        en2.draw()

        # 3. RECTANGLE BLEU INFÉRIEUR GAUCHE 
        en3 = c31.Rectangle(VueJeu.canvasBase, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
        en3.draw()

        # 4. RECTANGLE BLEU INFÉRIEUR DROIT 
        en4 = c31.Rectangle(VueJeu.canvasBase, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
        en4.draw()


class CarreRouge() :

    # CRÉATION DU CARRÉ ROUGE 
    carreRouge = tk.Canvas(VueMenu.root, width=40, height=40, background="red")
    carreRouge.place(x=420, y=250, anchor=tk.CENTER)
     # CACHE LE CURSEUR SUR LE CARREÉ ROUGE
    carreRouge.config(cursor="none")

    

class Mouvement:

    # CHAQUE ENEMIE À SON PROPRE MOUVEMENT (le sens de direction)
    def mvt1(forme): 
        forme.translate(c31.Vecteur(0,4))
        Rectangle.enemie1.draw()
                
    def mvt2(forme): 
        forme.translate(c31.Vecteur(4,0))
        Rectangle.draw()

    def mvt3(forme): 
        forme.translate(c31.Vecteur(0,-2))
        Rectangle.draw() 
                
    def mvt4(forme): 
        forme.translate(c31.Vecteur(-4,-2))
        Rectangle.draw() 

    # EXÉCUTE APRÈS UN CERTAIN TEMPS
    def loop1() :
    # LOOP POUR LE RECTANGLE EN HAUT, À DROITE
        loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt1, Rectangle.enemie.en1), 50) 
        loop1.start()
    # LOOP POUR LE RECTANGLE EN HAUT, À GAUCHE
    def loop2():
        loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt2, Rectangle.enemie.en2), 50)
        loop2.start()
    # LOOP POUR LE RECTANGLE EN BAS, À DROITE
    def loop3():
        loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt3, Rectangle.enemie.en3), 50)
        loop3.start()
    # LOOP POUR LE RECTANGLE EN BAS, À GAUCHE      
    def loop4():
        loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt4, Rectangle.enemie.en4), 50)
        loop4.start()