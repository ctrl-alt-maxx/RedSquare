import tkinter as tk
 
class BounceTest():
    def __init__(self):
        self.running=True
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width = 400, height = 300)
        self.canvas.grid()
 
        self.x0 = 10
        self.y0 = 50
        self.x1 = 60
        self.y1 = 100
        self.deltax = 2
        self.deltay = 3
        self.which=self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1,
                                      fill="red", tag='red_ball')
 
        tk.Button(self.window, text="Stop/Start Ball", bg='yellow',
               command=self.stop_it).grid(row=1, column=0)
        tk.Button(self.window, text="Exit", bg='orange',
               command=self.window.quit).grid(row=2, column=0)
        self.window.after(50, self.move_the_ball)
 
        self.window.mainloop()
 
    def move_the_ball(self):
        if self.running:
            self.canvas.move(self.which, self.deltax, self.deltay)
            ## check for ball hitting edges & change direction
            if self.x1 >= 400:
               self.deltax = -2
            if self.x0 < 0:
               self.deltax = 2
            if self.y1 > 290:
                self.deltay = -3
            if self.y0 < 0:
                self.deltay = 3
 
            ## keep track of the coordinates to tell when
            ## the ball moves off canvas
            self.x0 += self.deltax
            self.x1 += self.deltax
            self.y0 += self.deltay
 
            self.window.after(25, self.move_the_ball)
 
    def stop_it(self):
        self.running=not self.running
        if self.running:
            self.move_the_ball()
 
if __name__ == "__main__":
    BounceTest() 