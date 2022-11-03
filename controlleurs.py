from functools import partial
import tkinter
from tkinter import messagebox as msg
import c31Geometry2 as c31
from modeles import Rectangle, Mouvement
from vues import VueJeu

class MenuController:
    
    # DETERMINE LA VITTESE DES FORMES BLEUES AU DÉBUT DU JEU
    class Difficulté:

        # PLUS LA VALEUR EST PETIT, PLUS LE MOUVEMENT EST DOUX
        # THE LOWER THE VALUE, THE CLEANNER THE MOVEMENT WITH FASTER SPEED
        defaultSpeed = 0 
        def Facile(self):
            self.defaultSpeed = 1000
        
            Mouvement.loop1, self.defaultSpeed
            Mouvement.loop2, self.defaultSpeed
            Mouvement.loop3, self.defaultSpeed
            Mouvement.loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()

        def Moyen(self):
            self.defaultSpeed = 200

            Mouvement.loop1, self.defaultSpeed
            Mouvement.loop2, self.defaultSpeed
            Mouvement.loop3, self.defaultSpeed
            Mouvement.loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()
            
        def Difficile(self):
            self.defaultSpeed = 50

            Mouvement.loop1, self.defaultSpeed
            Mouvement.loop2, self.defaultSpeed
            Mouvement.loop3, self.defaultSpeed
            Mouvement.loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()
        
    d = Difficulté()

    class JeuController:

        

    instruction()