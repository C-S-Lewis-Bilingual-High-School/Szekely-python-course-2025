import tkinter,random
w = tkinter.Tk()
p = tkinter.Canvas()
p.pack()

x = random.randint(10,500) #zaciatocna vodorovna suradnica
y = random.randint(10,300) #zaciatocna zvisla suradnica

p.create_rectangle(x, y, x + 50, y + 50, fill="red") #hlavny
p.create_rectangle(x + 20,y + 10, x + 30, y + 40, fill ="white", outline="white") #zvisly
p.create_rectangle(x + 10 ,y + 20, x + 40, y + 30, fill="white", outline="white") #vodorovny


"""
x = random.randint(10,100)
y = random.randint(10,100)
velkost =  random.randint(10,100)

p.create_rectangle(x, y, x + velkost, y + velkost)
"""



w.mainloop()