from functools import partial
from tkinter import Canvas
import tkinter as tk
import c31Geometry2 as c31
import random
from tkinter import messagebox as msg
import csv
import datetime as dt


root = tk.Tk()

# COULEUR DE FOND
root.config(background="LightSkyBlue1")

# AJOUTER UN TITRE À LA FENÊTRE TKINTER
root.title("Jeu du carré rouge")

# FIXDE LA TAILLE EN PIXEL
root.geometry("850x850")




# CRÉATION DES RECTANGLES/ENEMIES

def enemie() : 
    # 1. RECTANGLE BLEU GAUCHE
    en1 = c31.Rectangle(canvasBase, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
    en1.draw()

    # 2. RECTANGLE BLEU SUPÉRIUR DROIT
    en2 = c31.Rectangle(canvasBase, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
    en2.draw()

    # 3. RECTANGLE BLEU INFÉRIEUR GAUCHE 
    en3 = c31.Rectangle(canvasBase, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
    en3.draw()

    # 4. RECTANGLE BLEU INFÉRIEUR DROIT 
    en4 = c31.Rectangle(canvasBase, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
    en4.draw()



# CRÉATION DU CARRÉ ROUGE 
carreRouge = tk.Canvas(root, width=40, height=40, background="red")
carreRouge.place(x=420, y=250, anchor=tk.CENTER)

# CACHE LE CURSEUR SUR LE CARREÉ ROUGE
carreRouge.config(cursor="none")

    

# CHAQUE ENEMIE À SON PROPRE MOUVEMENT (le sens de direction)
def mvt1(forme): 
    forme.translate(c31.Vecteur(0,4))
    enemie.en1.draw()
                
def mvt2(forme): 
    forme.translate(c31.Vecteur(4,0))
    enemie.en2.draw()

def mvt3(forme): 
    forme.translate(c31.Vecteur(0,-2))
    enemie.en3.draw()
                
def mvt4(forme): 
    forme.translate(c31.Vecteur(-4,-2))
    enemie.en4.draw() 

# EXÉCUTE APRÈS UN CERTAIN TEMPS
def loop1() :
    loop1 = c31.LoopEvent(canvasBase, partial(mvt1, enemie.en1), 50) 
    loop1.start()

def loop2():
    loop2 = c31.LoopEvent(canvasBase, partial(mvt2, enemie.en2), 50)
    loop2.start()

def loop3():
    loop3 = c31.LoopEvent(canvasBase, partial(mvt3, enemie.en3), 50)
    loop3.start()
            
def loop4():
    loop4 = c31.LoopEvent(canvasBase, partial(mvt4, enemie.en4), 50)
    loop4.start()

################





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
    menubar = tk.Menu(root)
    root.config(menu=menubar)

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
    file_menu.add_command(label='Quitter', command=root.destroy)

    # AJOUTER LE FILE_MENU AU MENUBAR
    menubar.add_cascade(
        label="Menu",
        menu = file_menu
    )
        


# PLUS LA VALEUR EST PETIT, PLUS LE MOUVEMENT EST DOUX
defaultSpeed = 0 
def Facile(self):
    self.defaultSpeed = 1000
        
    loop1, self.defaultSpeed
    loop2, self.defaultSpeed
    loop3, self.defaultSpeed
    loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()

def Moyen(self):
    self.defaultSpeed = 200

    loop1, self.defaultSpeed
    loop2, self.defaultSpeed
    loop3, self.defaultSpeed
    loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

            #loop1.start()
            #loop2.start()
            #loop3.start()
            #loop4.start()
            
def Difficile(self):
    self.defaultSpeed = 50

    loop1, self.defaultSpeed
    loop2, self.defaultSpeed
        Mouvement.loop3, self.defaultSpeed
        Mouvement.loop4, self.defaultSpeed

            #loop1 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt1, Rectangle.enemie1), self.defaultSpeed)
            #loop2 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt2, Rectangle.enemie2), self.defaultSpeed)
            #loop3 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt3, Rectangle.enemie3), self.defaultSpeed)
            #loop4 = c31.LoopEvent(canvasBase, partial(Mouvement.mvt4, Rectangle.enemie4), self.defaultSpeed)

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

    # FONCTION POUR TRAÎNER (drag) LE CARRÉ ROUGE 
    def trainer(event) :
        event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)

    CarreRouge.bind("<B1-Motion>", trainer)

################




class VueMenu:

    # AFFICHAGE DES CONSIGNES 
    def instruction():
        msg.showinfo(title="Instruction", message="Cliquez et maintenez le carré rouge le plus longtemps possible.")

    instruction()


class VueJeu:

    #CRÉATION DU CANVAS
    canvasBase = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black") 
    canvasBase.pack()

    def destroy(self):
        self.canvas.destroy()
        

    def enregistrerScores():
        d = dt.datetime.now()
        t = random.randrange(1, 21)
        name = "Marc"

        # FICHIER CONTENANT LES TEMPS DES PARTIES PRÉCEDENTES
        f = open("scores.csv", "a")
        with f:
            fnames = ['Nom', 'Temps', 'Date Joué']
            csvwriter = csv.DictWriter(f, fieldnames=fnames)
            csvwriter.writerow( {'Nom' : name, 'Temps' : t, 'Date Joué' : d} ) 
        f.close()

    def montrerScores():
        # RÉPONSE POUR SI L'UTILISATEUR VEUT VOIR LES TEMPS PRÉCEDENTS
        reponse = msg.askyesno("Question","Voulez-vous voir le temps des parties précédentes?")

        if reponse == True :
            score = tk.Tk()
            score.title('Tkinter Scores')
            score.geometry('800x400')
            
            col_noms = ("Username", "Temps", "Date Joué")
            for i, col_name in enumerate(col_noms, start=0):
                tk.Label(score, text=col_name).grid(row=0, column=i, padx=40)
                
            # ACCÈS AU FICHIER
            with open("scores.csv", "r", newline="\n") as scorefile:
                reader = csv.reader(scorefile)
                data = list(reader)
                
            scoresliste = []
            for i, row in enumerate(data):
                scoresliste.append(row[0])
                for col in range(0, 3):
                    tk.Label(score, text=row[col]).grid(row=i+1, column=col, padx=100)
                    
            score.mainloop()




root.mainloop()

    

    