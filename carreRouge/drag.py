import tkinter as tk 
from tkinter import  *
import c31Geometry2 as geo

c31 = geo
my_w = tk.Tk()
my_w.geometry("450x450")  # width and height 
def my_callback(event):
     l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
     
     
# def mvt(form):
#     form.translate(c31.Vector(4,0))
#     form.draw()     

my_w.title("Mouvement du carree rouge")

l1 = tk.Label(my_w, text='to Display',bg='yellow',font=30)
l1.pack(padx=30,pady=30)

my_w.bind('<B1-Motion>',my_callback) # Mouse left button pressed move
my_w.mainloop()