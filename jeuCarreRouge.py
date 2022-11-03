from tkinter.ttk import Frame
from controlleurs import MenuController, JeuController
import tkinter as tk

# BOUCLE DU JEU
if __name__ == "__main__" :
    root = tk.Tk()

    # COULEUR DE FOND
    root.config(background="LightSkyBlue1")

    # AJOUTER UN TITRE À LA FENÊTRE TKINTER
    root.title("Jeu du carré rouge")

    # FIXDE LA TAILLE EN PIXEL
    root.geometry("850x850")

    # CRÉATION DE LA FRAME DE MENU
    frameMenu = tk.Frame(root)
    frameMenu.pack()    # column=0, row=0

    # CRÉATION DE LA FRAME DE JEU
    frameJeu = tk.Frame(root)
    frameMenu.pack()    # column=1, row=0, columnspan=11, rowspan=11

    jeu = JeuController(root, None)
    menu = MenuController(frameMenu, root.destroy, jeu)

    menu.start()

    root.mainloop()