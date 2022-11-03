import tkinter as tk
my_w = tk.Tk()
width,height=410,210 # set the variables 
c_width,c_height=width-10,height-45 # canvas width height
d=str(width)+"x"+str(height)
my_w.geometry(d) 
c1 = tk.Canvas(my_w, width=c_width, height=c_height,bg='lightgreen')
c1.grid(row=1,column=0,padx=5,pady=5)
step=5 # value of each incremental movment, change this 
x1,y1=5,int(c_height/2) # starting position 
x2,y2=x1+15,y1+15      # starting position 
r1=c1.create_rectangle(x1, y1, x2,y2,fill='red')  # draw rectangle 
def my_draw():        
    global x1,y1,x2,y2,r1    
    c1.delete(r1) # delete the rectangle         
    r1=c1.create_rectangle(x1, y1, x2,y2,fill='red')    
    if (x2<(c_width-step)): # check for right edge          
        x1,x2=x1+step,x2+step # new coordinates of rectangle        
        c1.after(100,my_draw)  # recursive call after delay           
    else:        
        return   # stop recursive call and return to main 

my_draw() # start moving, remove this if not required at beginning 

def restart():    
    global x1,y1,x2,y2    
    x1,y1=5,int(c_height/2) # starting position     
    x2,y2=x1+15,y1+15      # starting position     
    my_draw() # start from starting position 
    b1=tk.Button(my_w,text='Restart',command=lambda:restart())b1.grid(row=2,column=0)

my_w.mainloop()
