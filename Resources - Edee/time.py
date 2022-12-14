from functools import partial
from os import stat
import tkinter as tk
from tkinter import ANCHOR, CENTER, Canvas, Label, Menu, StringVar
from tkinter import messagebox as msg
from tracemalloc import start, stop
import c31Geometry2 as c31
import time 
from datetime import date, datetime
import re

root = tk.Tk()

# Background color
root.config(background="royalblue")

# Ajouter un titre a la fenetre TK
root.title("Jeu du carré rouge")

# Fixe la taille de la fenetre en pixel
root.geometry("1000x1000")

# Creating canvas 
canvas = tk.Canvas(root, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")

#canvas = c31.Carre(root, c31.Vecteur(450,450), 450, bordure="black", remplissage="white", epaisseur=50)

# Creating rectangles
# 1. rectangle bleu gauche
rectangle1 = c31.Rectangle(canvas, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
rectangle1.draw()

# 2. rectangle bleu superieur droit
rectangle2 = c31.Rectangle(canvas, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
rectangle2.draw()

# 3. rectangle bleu inferieur gauche 
rectangle3 = c31.Rectangle(canvas, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
rectangle3.draw()

# 4. rectangle bleu infereieur droit 
rectangle4 = c31.Rectangle(canvas, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
rectangle4.draw()

canvas.pack()

def log(var, e):
    print(var)


#carre = c31.Carre(canvas, c31.Vecteur(225, 225), 40, remplissage="red")
#carre.draw()

loop = c31.LoopEvent(root, partial(log, "Cliquez-Loop", None), 1000)
# loop.start()

def mvt(forme):
    forme.translate(c31.Vecteur(4, 0))
    #forme.translateTo(c31.Vecteur(4,0), c31.Vecteur(5,10))
    forme.draw()
    forme.translate(c31.Vecteur(5, 10))
    
# Mouvement du carree rouge on its own
# loop2 = c31.LoopEvent(canvas, partial(mvt, carre))
# loop2.start()

def log(var, e):
    print(var)

loop = c31.LoopEvent(root, partial(log, "Cliquez-loop", None), 1000)
# loop.start()

# POP_UP - RIGHT-CLICK

label = Label(root)
label.pack()

# Ajout du menu
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

# Button 2 for MAC, buttonPress-3 for windows 
root.bind("<ButtonPress-2>", rightClickMenu)
root.bind(canvas, "<ButtonPress-1>", partial(print, "allo"))
root.bind("<ButtonPress-1>", partial(print, "pressed"))
root.bind("<ButtonRelease>", partial(print, "released"))
root.bind("<B1-Motion>", partial(print, "dragged"))

def drag(event) :
    event.widget.place(x=event.x_root, y=event.y_root, anchor=CENTER)
    

carre2 = Canvas(root, width=40, height=40, bg="red")
carre2.place(x=225, y=225, anchor=CENTER)

#def timer(drag, mouseReleased) :
#    startTime = time.time()
    #endTime = time.time()
##    time_lapsed = round((time.time() - startTime), 2)
#    while (drag) :
#        time_lapsed
#        print("Total Time:" + str(time_lapsed))
#        if (mouseReleased) :
#            time_lapsed

def timeStamp(drag) :

    # Timer starts
    starttime = time.time()
    lasttime = starttime
    lapnum = 1
   
    while (drag) :
        # The current lap-time
        laptime = round((time.time() - lasttime), 2)
  
        # Total time elapsed since the timer started
        totaltime = round((time.time() - starttime), 2)
  
        # Printing the lap number, lap-time, and total time
        print("Lap No. "+str(lapnum))
        print("Total Time: "+str(totaltime))
        print("Lap Time: "+str(laptime))
    
        # Updating the previous total time and lap number
        lasttime = time.time()
        lapnum += 1

def calculerTime() :
    today = datetime.now()
    startTime_string = today #.strftime("%H:%M:%S")
    print(startTime_string)

    if startTime_string == datetime(2022,10,31,19,15,00) :
        newToday = datetime.now()
        endTime_string = newToday #.strftime("%H:%M:%S")
        print(endTime_string)
    else :
        endTime_string = datetime(2022,10,31,20,10,00)
    
    timer = endTime_string - startTime_string
    print(timer)
    

calculerTime()

carre2.bind("<B1-Motion>", drag)

# prompt window 
# msg.showinfo("You've survived " + str(timer) + " secondes!")

root.mainloop()