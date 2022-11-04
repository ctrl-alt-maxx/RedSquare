from tkinter import Tk
from tkinter.messagebox import Message 
from _tkinter import TclError

TIME_TO_WAIT = 10000 # in milliseconds 
root = Tk() 
root.withdraw()
try:
    root.after(TIME_TO_WAIT, root.destroy) 
    Message(title="your title", message="your message", master=root).show()
except TclError:
    pass