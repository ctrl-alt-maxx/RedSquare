
from functools import partial
from tkinter import *
from tkinter.ttk import *
from tkinter import Canvas, Label, Menu, Tk, ttk
from turtle import width
import c31Geometry2 as c31
import truefalse as TS
import shapes as SH
import time as t
from random import * #lambda: randint(2, 6) > 1


# VVVVVV CAN MODIFY FROM THIS POINT VVVVV
class Mouvement:
    
    step1 = 1
    step2 = 5
    step3 = 10 

    def mvt(forme): 
        
        forme.translate(c31.Vecteur(0,4))
        SH.rectangle1.draw()
        
            
            
    def mvt2(forme): 
        forme.translate(c31.Vecteur(4,0))
        SH.rectangle2.draw()

    def mvt3(forme): 
        forme.translate(c31.Vecteur(0,-2))
        SH.rectangle3.draw() 
        
    def mvt4(forme): 
        forme.translate(c31.Vecteur(-4,-2))
        SH.rectangle4.draw() 

    loop = c31.LoopEvent(SH.canvas,partial(mvt,SH.rectangle1),50) 
    loop.start()

    loop2 = c31.LoopEvent(SH.canvas,partial(mvt2,SH.rectangle2),50)
    loop2.start()

    loop3 = c31.LoopEvent(SH.canvas,partial(mvt3,SH.rectangle3),50)
    loop3.start()
    
    loop4 = c31.LoopEvent(SH.canvas,partial(mvt4,SH.rectangle4),50)
    loop4.start()



    SH.root.mainloop()



