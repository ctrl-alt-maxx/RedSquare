from os import stat
from time import time
from tkinter import *
from tracemalloc import start
import time


def buttonPressed( event ):
   var.set( "Pressed at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

def buttonReleased( event ):
   var.set( "Released at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

def enteredWindow( event ):
   var.set( "Mouse in window" )

def exitedWindow(  event ):
   var.set( "Mouse outside window" )

def mouseDragged( event ):
   var.set( "Dragged at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

#def timer(mouseDragged) :
#   startTime = time.time()
#   while (mouseDragged) :
#      totalTime = round((time.time() - startTime), 2)
#      print(totalTime)

base = Tk()
base.title("Mouse Events")


frame = Frame(base, width=300, height=300)
frame.pack()

var = StringVar()
var.set("Mouse Events will show here")
label = Label(base, textvariable=var)
label.pack(side=BOTTOM)

frame.bind( "<Button-1>", buttonPressed )
frame.bind( "<ButtonRelease-1>", buttonReleased )   
frame.bind( "<Enter>", enteredWindow )
frame.bind( "<Leave>", exitedWindow )
frame.bind( "<B1-Motion>", mouseDragged )
#frame.bind("<B1-Motion>", timer)

#if (frame.bind("<ButtonRelease-1>", buttonReleased)) :
#   (frame.bind("<Leave>"), timer)



base.mainloop()