import tkinter as tk


def draw_picture1(canvas):
    canvas.create_rectangle(0, 0, 100, 100)
    canvas.create_oval(25, 25, 75, 75)


def draw_picture2(canvas):
    canvas.create_rectangle(0, 0, 100, 100)
    canvas.create_oval(110, 0, 210, 100)


def draw_picture3(canvas):
    canvas.create_rectangle(0, 0, 100, 100)
    canvas.create_oval(-30, 20, 30, 80)


def draw_picture4(canvas):
    canvas.create_rectangle(0, 0, 100, 100)
    canvas.create_oval(50, 50, 150, 150)


def main():
    root = tk.Tk()
    root.title("Tkinter Picture Generator")
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    draw_picture1(canvas)
    draw_picture2(canvas)
    draw_picture3(canvas)
    draw_picture4(canvas)

    root.mainloop()


if __name__ == "__main__":
    main()
