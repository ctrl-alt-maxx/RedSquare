import time 
from time import sleep
import tkinter as tk
from tkinter import messagebox as msg
import datetime as dt
import csv
import random


def Jeu():
    while True:
        root = tk.Tk()
        root.title('Tkinter Game')
        # root.resizable(False, False)
        root.geometry('800x800')
        
        anon = msg.askyesno("Question", "Voulez-vous mettre votre nom?")
        d = dt.datetime.now()
        if anon == False:
            name = "Joueur Anonyme"
        else:
            # time.sleep(2)
            id = tk.Tk()
            id.title("Identifiant")
            id.resizable(False, False)
            id.geometry("300x200")
            tk.Label(id, text="Écrie ton nom").grid(row=0)
            e = tk.Entry(id)
            e.grid(row=0, column=1)
            
            tk.Button(id, text="Enregistrer", command=id.quit).grid(row=3, column=0)
            id.mainloop()
            name = e.get()
            id.destroy()
            
        # name = "Marc"
        t = random.randrange(1,21)
        # FICHIER CONTENANT LES TEMPS DES PARTIES PRÉCEDENTES
        f = open("score.csv", "a")
        with f:
            fnames = ['Nom', 'Temps', 'Date']
            csvwriter = csv.DictWriter(f, fieldnames=fnames)
            csvwriter.writerow( {'Nom' : name, 'Temps' : t, 'Date' : d} ) 
        f.close()

        # RÉPONSE POUR SI LA PERSONNE VEUT VOIR LES TEMPS PRÉCEDENTS
        answer = msg.askyesno("Question","Voulez-vous voir le temps des autres parties?")
        
        if answer == True :
            score = tk.Tk()
            score.title('Tkinter Scores')
            # score.resizable(True, True)
            score.geometry('800x400')
            
            col_names = ("Joueur", "Temps Survécu (secondes)", "Date Joué")
            for i, col_name in enumerate(col_names, start=0):
                tk.Label(score, text=col_name).grid(row=0, column=i, padx=40)
                
            # ACCÈS AU FICHIER
            with open("score.csv", "r", newline="\n") as scorefile:
                reader = csv.reader(scorefile)
                data = list(reader)
                
            scoreslist = []
            for i, row in enumerate(data):
                scoreslist.append(row[0])
                for col in range(0, 3):
                    tk.Label(score, text=row[col]).grid(row=i+1, column=col, padx=100)      
            score.mainloop()        
                            
        # RÉPONSE POUR SI LA PERSONNE VEUT FAIRE UNE AUTRE PARTIE
        answer2 = msg.askyesno("Rejouer", "Voulez-vous rejoué?")
        root.mainloop()
        if answer2 == False:
            root.destroy()
        else:
            Jeu()
        
Jeu()