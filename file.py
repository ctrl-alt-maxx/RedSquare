from ctypes.wintypes import SIZE
from time import time
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import datetime as dt
import csv
import random
from tracemalloc import start


root = tk.Tk()
root.title('Tkinter File')
root.resizable(False, False)
root.geometry('800x800')
d = dt.datetime.now()
# fd.askopenfilename(initialdir="x:/C31-Genie Logiciel/carreRouge/wow.txt", title="Open Text File", filetypes=(("Text Files", "*.txt"),))

# name = "Marc"
# t = random.randrange(1,21)
# f = open("x:/C31-Genie Logiciel/carreRouge/wow.csv", "a")
# #print(f.read())
# with f:
#     fnames = ['Nom', 'Temps', 'Annee', 'Mois', 'Jour']
#     csvwriter = csv.DictWriter(f, fieldnames=fnames)
#     csvwriter.writerow( {'Nom' : name, 'Temps' : t, 'Annee' : d.year, 'Mois' : d.month, 'Jour' : d.day} ) 
# f.close()

answer = msg.askyesno("Question","Do want to see other scores?")


# print(answer)
if answer == True :
    col_names = ("Username", "Name", "Date Created","i","j")
    for i, col_name in enumerate(col_names, start=1):
        tk.Label(root, text=col_name).grid(row=3, column=i, padx=40)
        
    # f = open()    
    with open("wow.txt", "r", newline="") as scorefile:
        reader = csv.reader(scorefile)
        data = list(reader)
        
    scoreslist = []
    for i, row in enumerate(data, start=4):
        scoreslist.append(row[0])
        
        for col in range(1,8):
            tk.Label(root, text=row[col]).grid(row=i, column=col)
        
    count = 0
    while count <= len(scorefile):
        print(scorefile[count])
        count += 1


root.mainloop()