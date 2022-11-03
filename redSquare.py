
from functools import partial
from tkinter import *
from tkinter.ttk import *
from tkinter import Canvas, Label, Menu, Tk, ttk
from turtle import width
import c31Geometry2 as c31
import truefalse as TS
import shapes as SH
import time as t



# VVVVVV CAN MODIFY FROM THIS POINT VVVVVV
class REC1:
    def __init__(self, master = None):
        self.master = master
         
        # to take care movement in x direction
        self.x = 1
        # to take care movement in y direction
        self.y = 1
 
        # canvas object to create shape
        self.canvas = SH.canvas
        # creating rectangle
        self.rectangle = SH.rectangle1
        self.canvas.pack()
 
        # calling class's movement method to
        # move the rectangle
        self.movement()
     
    def movement(self):
 
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.canvas.move(self.rectangle, self.x, self.y)
 
        self.canvas.after(100, self.movement)
        
    
     
    
    if __name__ == "__main__":
        master = Tk()
       
   
        mainloop()
     
    

# def mvt(forme): 
    
#     forme.translate(c31.Vecteur(0,7))
#     SH.rectangle2.draw()
    
        
        
# # def mvt2(forme): 
# #     forme.translate(c31.Vecteur(-10,9.5))
# #     SH.rectangle2.draw()

# # def mvt3(forme): 
# #     forme.translate(c31.Vecteur(2,2))
# #     SH.rectangle2.draw()  


# loop = c31.LoopEvent(SH.canvas,partial(mvt,SH.rectangle2),100) 
# loop.start()

# # loop2 = c31.LoopEvent(SH.canvas,lambda: randint(1, 2) > 1,partial(mvt2,SH.rectangle2),100)
# # loop2.start()

# # loop3 = c31.LoopEvent(SH.canvas,lambda: randint(2, 4) > 1,partial(mvt3,SH.rectangle2),100)
# # loop3.start()

# ##def update():
#       #SH.rectangle2.draw() 
    
# # # if SH.rectangle2.get_position() == c31.Vecteur(300,95) :
# # #         TS.go = bool(False)
# # # else: 
# # #     loop.start() 

         
 
# #update() 

    
# #e = c31.LoopEvent(SH.root, update, 100)
# #e.startImmediately() 

# SH.root.mainloop()



