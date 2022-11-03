from functools import partial
import tkinter
from tkinter import messagebox as msg
import c31Geometry2 as c31
from modeles import Rectangle
from vues import VueJeu

class MenuController:
    
    # DETERMINE LA VITTESE DES FORMES BLEUES AU DÉBUT DU JEU
    class Difficulté:
        defaultSpeed = 0 # THE LOWER THE VALUE, THE CLEANNER THE MOVEMENT WITH FASTER SPEED
        def Facile(self):
            self.defaultSpeed = 1000
        
            loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt1, Rectangle.rectangle1), self.defaultSpeed)
            loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt2, Rectangle.rectangle2), self.defaultSpeed)
            loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt3, Rectangle.rectangle3), self.defaultSpeed)
            loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt4, Rectangle.rectangle4), self.defaultSpeed)

            loop1.start()
            loop1.start()
            loop2.start()
            loop3.start()
            loop4.start()

        def Moyen(self):
            self.defaultSpeed = 200

            loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt1, Rectangle.rectangle1), self.defaultSpeed)
            loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt2, Rectangle.rectangle2), self.defaultSpeed)
            loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt3, Rectangle.rectangle3), self.defaultSpeed)
            loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt4, Rectangle.rectangle4), self.defaultSpeed)

            loop1.start()
            loop2.start()
            loop3.start()
            loop4.start()
            
        def Difficile(self):
            self.defaultSpeed = 50

            loop1 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt1, Rectangle.rectangle1), self.defaultSpeed)
            loop2 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt2, Rectangle.rectangle2), self.defaultSpeed)
            loop3 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt3, Rectangle.rectangle3), self.defaultSpeed)
            loop4 = c31.LoopEvent(VueJeu.canvasBase, partial(mvt4, Rectangle.rectangle4), self.defaultSpeed)

            loop1.start()
            loop2.start()
            loop3.start()
            loop4.start()
        
    d = Difficulté()

    instruction()