
import random
import tkinter as tk
from tkinter import messagebox as msg
import csv
import datetime as dt
from jeuCarreRouge import root1


class VueMenu:

    # AFFICHAGE DES CONSIGNES 
    def instruction():
        msg.showinfo(title="Instruction", message="Cliquez et maintenez le carré rouge le plus longtemps possible.")

    instruction()

    #def draw(self) :
    #    self.btn_nouvellePartie.pack()
    #    self.btn_quitApp.pack()

    #def setListen(self, eventName, command) :
    #    self.root.bind(eventName, command)


class VueJeu:
    #def __init__(self, root) :
    #    self.root = root
    #    self.playerIndication = tk.Label(root, text="Cliquez sur \"Nouvelle partie\" pour commencer.")

    #CRÉATION DU CANVAS
    canvasBase = tk.Canvas(root1, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black") 
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

    #def messageBox(self, msg, title = "", typeBox = "yesno") :
    #    if typeBox == "yesno" :
    #        return msg.messagebox.askquestion(title, msg) == "yes"
    #    else :
    #        msg.messagebox.showinfo(title, msg)
    #        return True


