import random
import tkinter
w = tkinter.Tk()
WIDTH = 600
HEIGHT = 600
p = tkinter.Canvas(width = WIDTH, height = HEIGHT)
p.pack()

x = 0
y = 0

n = random.randint(1,100)
a = WIDTH / n      #rozmer stvorceka

for j in range(n):
    for i in range(n):
        p.create_rectangle(x,y,x + a,y + a)
        x += a

    y = y + a
    x = 0



w.mainloop()