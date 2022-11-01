from time import time
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import datetime as dt
import csv
import random


root = tk.Tk()
root.title('Tkinter File')
root.resizable(False, False)
root.geometry('450x450')
d = dt.datetime.now()
# fd.askopenfilename(initialdir="x:/C31-Genie Logiciel/carreRouge/wow.txt", title="Open Text File", filetypes=(("Text Files", "*.txt"),))

name = "Marc"
t = random.randrange(1,21)
f = open("x:/C31-Genie Logiciel/carreRouge/wow.csv", "a")
#print(f.read())
with f:
    fnames = ['Nom', 'Temps', 'Annee', 'Mois', 'Jour']
    csvwriter = csv.DictWriter(f, fieldnames=fnames)
    csvwriter.writerow( {'Nom' : name, 'Temps' : t, 'Annee' : d.year, 'Mois' : d.month, 'Jour' : d.day} ) 
f.close()

answer = msg.askyesno("Question","Do want to see other scores?")
print(answer)
if answer == True :
    f = open("x:/C31-Genie Logiciel/carreRouge/wow.csv", "r")
    print(f.read())
    f.close()
root.mainloop()