import tkinter as tk
from tkinter import messagebox as msg
import datetime as dt
import csv
import random

root = tk.Tk()
root.title('Tkinter Game')
root.geometry('800x800')
d = dt.datetime.now()

# name = "Marc"
# t = random.randrange(1,21)

# # FICHIER CONTENANT LES TEMPS DES PARTIES PRÉCEDENTES
# f = open("wow.txt", "a")
# with f:
#     fnames = ['Nom', 'Temps', 'Date Joué']
#     csvwriter = csv.DictWriter(f, fieldnames=fnames)
#     csvwriter.writerow( {'Nom' : name, 'Temps' : t, 'Date Joué' : d} ) 
# f.close()

# RÉPONSE POUR SI LA PERSONNE VEUT VOIR LES TEMPS PRÉCEDENTS
answer = msg.askyesno("Question","Veux-tu voir le temps des autres parties?")

if answer == True :
    score = tk.Tk()
    score.title('Tkinter Scores')
    score.resizable(True, False)
    score.geometry('800x400')
    
    col_names = ("Username", "Temps", "Date Joué")
    for i, col_name in enumerate(col_names, start=0):
        tk.Label(score, text=col_name).grid(row=0, column=i, padx=40)
        
    # ACCÈS AU FICHIER
    with open("wow.txt", "r", newline="\n") as scorefile:
        reader = csv.reader(scorefile)
        data = list(reader)
        
    scoreslist = []
    for i, row in enumerate(data):
        scoreslist.append(row[0])
        for col in range(0, 3):
            tk.Label(score, text=row[col]).grid(row=i+1, column=col, padx=100)
            
    score.mainloop()        
            
root.mainloop()            
