
import tkinter as tk
import c31Geometry2 as c31
from modeles import Mouvement, CarreRouge
from vues import VueMenu, VueJeu

class MenuController:
    def __init__(self, root, closeApp, jeuControler) :
        self.jeuControler =jeuControler
        self.vue = VueMenu(root, self.nouvellePartie(), closeApp)

    def start(self) :
        # AFFICHE LE MENU 
        #VueMenu.instruction()
        #VueMenu.menu()
        #return self.start()
        self.vue.draw()

    def nouvellePartie(self) :
        if self.jeuControler.getStartedMatchState() :
            root = self.jeuControler.vue.root
            vue = self.jeuControler.vue
            self.jeuControler.vue.destroy
            self.jeuControler = JeuController(root, vue)
        
        self.jeuControler.start()
        self.jeuControler.nouvellePartie

    def menu():
        # CRÉATION D'UN MENUBAR
        menubar = tk.Menu(VueMenu.root)
        VueMenu.root.config(menu=menubar)

        # CRÉATION DU FILE_MENU
        file_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        # AJOUTER DES ITEMS DANS LE MENU
        file_menu.add_command(label='Facile', command=MenuController.d.Facile)
        file_menu.add_command(label='Moyen', command=MenuController.d.Moyen)
        file_menu.add_command(label='Difficle', command=MenuController.d.Difficile)
        file_menu.add_separator()
        file_menu.add_command(label='Quitter', command=VueMenu.root.destroy)

        # AJOUTER LE FILE_MENU AU MENUBAR
        menubar.add_cascade(
            label="Menu",
            menu = file_menu
        )
        
class Difficulté:

    # PLUS LA VALEUR EST PETIT, PLUS LE MOUVEMENT EST DOUX
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
    def __init__(self, root, vue) :
        self.partieDemarrer = False
        self.nouvellePartieFct = lambda : print("Nouvelle partie")
        self.vue = VueJeu(root)
        self.__defineEvent()

    def getStatedMatchState(self) :
        return self.partieDemarrer

    #def __defineEvent(self) :
    #    self.vue.setListen("<B1-Motion>")
    #    self.CarreRouge.bind("<B1-Motion>", self.trainer)
        # CACHE LE CURSEUR SUR LE CARREÉ ROUGE
    #    self.CarreRouge.config(cursor="none")

    

    #def start(self) :
    #    self.partieDemarrer = True
    #    self.vue.draw()

    # FONCTION POUR TRAÎNER (drag) LE CARRÉ ROUGE 
    def trainer(event) :
        event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)

    CarreRouge.bind("<B1-Motion>", trainer)

    

    

    