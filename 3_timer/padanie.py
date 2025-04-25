import tkinter

w = tkinter.Tk()
p = tkinter.Canvas(width = 600, height = 400)
p.pack()

x = 300
y = 0

p.create_oval(x,y,x+10,y+10)

def casovac():
    global y, x
    y = y + 10
    p.delete("all")
    p.create_oval(x,y,x+10,y+10)
    p.update()

    if y < 400:
        p.after(100, casovac)

casovac()

w.mainloop()