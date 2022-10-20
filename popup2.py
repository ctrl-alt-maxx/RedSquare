#Import the required libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of the Tkinter library
win.geometry("700x350")

label = Label(win, text="Right-click anywhere to display a menu", font= ('Helvetica 18'))
label.pack(pady= 40)

#Add Menu
popup = Menu(win, tearoff=0)

#Adding Menu Items
popup.add_command(label="New")
popup.add_command(label="Edit")
popup.add_separator()
popup.add_command(label="Save")

def menu_popup(event):
   # display the popup menu
   try:
      popup.tk_popup(event.x_root, event.y_root, 0)
   finally:
      #Release the grab
      popup.grab_release()

win.bind("<Button-2>", menu_popup)

button = ttk.Button(win, text="Quit", command=win.destroy)
button.pack()

mainloop()