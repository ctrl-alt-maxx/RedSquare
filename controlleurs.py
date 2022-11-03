from functools import partial
import tkinter as tk
from tkinter import messagebox as msg
import c31Geometry2 as c31
from modeles import CarreRouge, Rectangle, Mouvement
from vues import VueJeu, VueMenu

class MenuController:
    def __init__(self, root, closeApp, jeuControler) :
        self.jeuControler =jeuControler
        self.vue = VueMenu(root, self.nouvellePartie(), closeApp)

    def start(self) :
        # AFFICHE LE MENU 
        VueMenu.instruction()
        VueMenu.menu()
    
        #return self.start()

    def nouvellePartie(self) :
        if self.jeuControler.getStartedMatchState() :
            root = self.jeuControler.vue.root
            vue = self.jeuControler.vue
            self.jeuControler.vue.destroy
            self.jeuControler = JeuController(root, vue)
        
        self.jeuControler.start()
        self.jeuControler.nouvellePartie

class JeuController:

    # FONCTION POUR TRAÎNER (drag) LE CARRÉ ROUGE 
    def trainer(event) :
        event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)

    CarreRouge.bind("<B1-Motion>", trainer)

    # CACHE LE CURSEUR SUR LE CARREÉ ROUGE
    CarreRouge.config(cursor="none")

    