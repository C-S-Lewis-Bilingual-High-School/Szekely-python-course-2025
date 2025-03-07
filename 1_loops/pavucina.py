import random
import tkinter
w = tkinter.Tk()
WIDTH = 600
HEIGHT = 600
p = tkinter.Canvas(width = WIDTH, height = HEIGHT)
p.pack()

x1 = 0
y1 = 0
x2 = WIDTH
y2 = 0

for i in range(WIDTH//10):
    p.create_line(x1,y1,x2,y2)
    x2 = x2 - 10
    y1 = y1 + 10

x = 0
y = 0
n = 1

for i in range(10):
    for j in range(n):
        p.create_rectangle(x,y,x+10,y+10)
        x = x + 10
    y = y + 10
    x = 0
    n = n + 1


w.mainloop()