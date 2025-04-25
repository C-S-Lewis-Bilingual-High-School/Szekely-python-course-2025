import tkinter, random

tk = tkinter.Tk()

WIDTH = 600
HEIGHT = 400
plocha = tkinter.Canvas(width = WIDTH, height = HEIGHT)
plocha.pack()

for i in range(10000):
    x = random.randint(1,WIDTH)
    y = random.randint(1,HEIGHT)
    if (y< 5* HEIGHT / 6) and (y > HEIGHT / 6):
        color = "blue"
    else:
        color = "white"

    plocha.create_oval(x-2,y-2,x+2,y+2,fill= color)


tk.mainloop()