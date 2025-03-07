import tkinter as tk


def draw_pattern_1(canvas):
    width, height = 200, 200
    for i in range(0, width, 10):
        canvas.create_line(width // 2, height, i, 0)

def draw_pattern_4(canvas):
    width, height = 200, 200
    for i in range(0, width, 10):
        canvas.create_line(width // 2, 0, i, height)


def draw_pattern_2(canvas):
    width, height = 200, 200
    for i in range(0, width, 10):
        canvas.create_line(0, 0, i, height)


def draw_pattern_3(canvas):
    width, height = 200, 200
    for i in range(0, width, 10):
        canvas.create_line(width, height, i, 0)


def main():
    root = tk.Tk()
    root.title("Line Patterns")

    frame = tk.Frame(root, bg='light yellow')
    frame.pack()

    canvases = []
    for i in range(4):
        canvas = tk.Canvas(frame, width=200, height=200, bg='white')
        canvas.grid(row=0, column=i, padx=5, pady=5)
        canvases.append(canvas)

    draw_pattern_1(canvases[0])
    draw_pattern_2(canvases[1])
    draw_pattern_3(canvases[2])
    draw_pattern_4(canvases[3])

    root.mainloop()


if __name__ == "__main__":
    main()
