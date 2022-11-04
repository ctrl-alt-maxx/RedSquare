import tkinter as tk
from tkinter import *

root = tk.Tk()
# root.geometry("450x450")
c = tk.Canvas(root, width=450, height=450)
c.create_rectangle(0, 450, 450, 0, fill="black") # BORDURE NOIRE
c.create_rectangle(50, 400, 400, 50, fill="white") 
c.create_rectangle(80, 80, 140, 140, fill="blue") # CARRE TOP-LEFT
c.create_rectangle(340, 60, 280, 110, fill="blue", outline="yellow") # CARRE TOP-RIGHT
c.create_rectangle(80, 320, 115, 380, fill="blue", outline="red") # RECTANGLE BOTTOM-LEFT
c.create_rectangle(280, 330, 399, 350, fill="blue", outline="green") # RECTANGLE BOTTOM-RIGHT
c.create_rectangle(180, 180, 225, 225, fill="red") # CARRE ROUGE
c.pack()

root.mainloop()