import tkinter
w = tkinter.Tk()
p = tkinter.Canvas(bg="white", width=600, height=400)

#mikrovlnka
p.create_rectangle(50,100,450,350, outline="blue")      #hlavna skrina
p.create_rectangle(100,150,350,300,fill="black")     #obsah vnutra
p.create_rectangle(375,275,425,300)     #tlacidlo

p.pack()
w.mainloop()

