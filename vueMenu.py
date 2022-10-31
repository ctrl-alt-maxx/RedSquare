
import tkinter as tk
from tkinter import Menu

root = tk.Tk()

# Couleur de fond
root.config(background="LightSkyBlue1")

# Ajouter un titre à la fenêtre TK
root.title("Jeu du carré rouge : Menu")

# Fixe la taille de la fenêtre en px
root.geometry("850x850")


# Texte pour afficher les consignes du jeu 
#texteTitre = tk.Label(root, text="Jeu du carré rouge", background="white", foreground="black", padx=300, pady=300)
#texteTitre.grid(column=10, row=11)

canvas = tk.Canvas(root, width= 450, height= 450, bg="SpringGreen2")
canvas.create_text(200, 200, text="Faites un clique droit pour afficher les niveaux de difficultés.", fill="black", font=('Helvetica 15 bold'))


canvas.pack()

rightClickMenu = Menu(root, tearoff=0)

# Adding items to the menu 
rightClickMenu.add_command(label="Facile")
rightClickMenu.add_command(label="Moyen")
rightClickMenu.add_command(label="Difficile")
rightClickMenu.add_separator()
rightClickMenu.add_command(label="Quitter", command=root.destroy)

def menu_rightClick(event):
    # Affichage du pop-up menu
    try:
        rightClickMenu.tk_popup(event.x_root, event.y_root)
    finally:
        # Release the grab
        rightClickMenu.grab_release()

root.bind("<ButtonPress-2>", rightClickMenu)

root.mainloop()

