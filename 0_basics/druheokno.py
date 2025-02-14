import tkinter,random
w = tkinter.Tk()
p = tkinter.Canvas()
p.pack()

for i in range(10):
    x = random.randint(10,500) #zaciatocna vodorovna suradnica
    y = random.randint(10,300) #zaciatocna zvisla suradnica
    v = random.randint(5,10) #velkost stvorceka v rastri
    print(i)
    p.create_rectangle(x, y, x + 5 * v, y + 5 * v, fill="red") #hlavny
    p.create_rectangle(x + 2 * v,y + 1 * v, x + 3 * v, y + 4 * v, fill ="white", outline="white") #zvisly
    p.create_rectangle(x + 1 * v ,y + 2 * v, x + 4 * v, y + 3 * v, fill="white", outline="white") #vodorovny


"""
x = random.randint(10,100)
y = random.randint(10,100)
velkost =  random.randint(10,100)

p.create_rectangle(x, y, x + velkost, y + velkost)
"""



w.mainloop()