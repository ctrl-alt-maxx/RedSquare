from tkinter import *
from tkinter.ttk import *
import c31Geometry2 as c31
 
class GFG:
    def __init__(self, master = None):
        self.master = master
         
        # to take care movement in x direction
        self.x = 0
        # to take care movement in y direction  
        self.y = 3
 
        # canvas object to create shape
        self.canvas = Canvas(master, background="white", width=450, height=450, highlightthickness=50, highlightbackground="black")
        # creating rectangle
        self.rectangle1 = self.canvas.create_rectangle(120, 120, 60, 60, fill = "blue")
        self.rectangle2 = self.canvas.create_rectangle(150, 47.5, 60, 50, fill = "blue")
        self.rectangle3 = self.canvas.create_rectangle(47.5, 150, 30, 60, fill = "blue")
        self.rectangle4 = self.canvas.create_rectangle(355/2, 340/2, 100, 60, fill = "blue")

        
        
        self.canvas.pack()
 
        # calling class's movement method to
        # move the rectangle
        self.movement()
        
     
    def movement(self):
 
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.canvas.move(self.rectangle1, self.x, self.y)
        self.canvas.after(100, self.movement)
      
     
    # def movement2(self):
    #     self.canvas.move(self.rectangle,self.x+3,self.y-3,)
    #     self.canvas.after(1000, self.movement)
        
 
if __name__ == "__main__":
 
    # object of class Tk, responsible for creating
    # a tkinter toplevel window
    master = Tk()
    
    master.config(background="royalblue")

    # Ajouter un titre a la fenetre TK
    master.title("Jeu du carré rouge")

    # Fixe la taille de la fenetre en pixel
    master.geometry("1000x1000") 
    
    gfg = GFG(master)
 

     
    # Infinite loop breaks only by interrupt
    mainloop()