# ** COMPLETER **
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
import c31Geometry2 as c31
from functools import partial

root = tk.Tk()



# Couleur de fond
root.config(background="LightSkyBlue1")

# Ajouter un titre à la fenêtre TK
root.title("Jeu du carré rouge : Menu")

# Fixe la taille de la fenêtre en px
root.geometry("850x850")

# Pour afficher les consignes 
L = tk.Label(root, text="Choississez un niveau de difficultés dans le menu.", width = 50, height = 20)
L.pack()

class VueMenu:
    def instruction():
        msg.showinfo(title="Instruction", message="Cliquez et maintenez le carré rouge le plus longtemps possible.")

    def menu():
        # Création d'un menuBar
        menubar = Menu(root)
        root.config(menu=menubar)

        # Creation du file_menu 
        file_menu = Menu(
            menubar,
            tearoff=0
        )

        # Ajouter des items dans le menu 
        file_menu.add_command(label='Facile', command=d.Facile)
        file_menu.add_command(label='Moyen', command=d.Moyen)
        file_menu.add_command(label='Difficle', command=d.Difficile)
        file_menu.add_separator()
        file_menu.add_command(label='Quitter', command=root.destroy)

        # Ajouter le file_menu au menuBar
        menubar.add_cascade(
            label="Menu",
            menu = file_menu
        )
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

class VueJeu:
    def canvasCreation():
        # Création du canvas 
        canvasBase = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")
        rectYellow = c31.Rectangle(canvasBase, c31.Vecteur(450, 450), 850, 850, remplissage="yellow")
        rectYellow.draw()


instruction()

root.mainloop()

