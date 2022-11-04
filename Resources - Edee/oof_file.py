import tkinter as tk
import csv

# Create and set the GUI for the passScreen of the Password Manager.
passScreen = tk.Tk()
passScreen.geometry("1200x800")
passScreen.resizable(width=False, height=False)
passScreen.title("Password")

col_names = ("Type", "Username", "Password", "Name", "Specific", "Date Created", "Date Updated")
for i, col_name in enumerate(col_names, start=1):
    tk.Label(passScreen, text=col_name).grid(row=3, column=i, padx=40)

with open("x:/C31-Genie Logiciel/carreRouge/PassManager.txt", "r", newline="") as passfile:
    reader = csv.reader(passfile)
    data = list(reader)

entrieslist = []
for i, row in enumerate(data, start=4):
    entrieslist.append(row[0])
    for col in range(1, 8):
        tk.Label(passScreen, text=row[col]).grid(row=i, column=col)

passScreen.mainloop()