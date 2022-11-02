
from functools import partial
import tkinter as tk
from tkinter import Canvas, Label, Menu, Tk, ttk
from turtle import width
import c31Geometry2 as c31
import truefalse as TS
import shapes as SH
import time as t




# VVVVVV CAN MODIFY FROM THIS POINT VVVVVV
def mvt(forme): 
    
    forme.translate(c31.Vecteur(0,2))
    SH.rectangle2.draw()
        
        
# def mvt2(forme): 
#     forme.translate(c31.Vecteur(-10,9.5))
#     SH.rectangle2.draw()

# def mvt3(forme): 
#     forme.translate(c31.Vecteur(2,2))
#     SH.rectangle2.draw()  


loop = c31.LoopEvent(SH.canvas,partial(mvt,SH.rectangle2),100) 
loop.start()

# loop2 = c31.LoopEvent(SH.canvas,lambda: randint(1, 2) > 1,partial(mvt2,SH.rectangle2),100)
# loop2.start()

# loop3 = c31.LoopEvent(SH.canvas,lambda: randint(2, 4) > 1,partial(mvt3,SH.rectangle2),100)
# loop3.start()

def update():
      SH.rectangle2.draw() 
    
# # if SH.rectangle2.get_position() == c31.Vecteur(300,95) :
# #         TS.go = bool(False)
# # else: 
# #     loop.start() 

         
 
#update() 

    
e = c31.LoopEvent(SH.root, update, 100)
e.startImmediately() 

SH.root.mainloop()



