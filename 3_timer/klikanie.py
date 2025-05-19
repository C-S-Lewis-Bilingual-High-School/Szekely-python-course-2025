import tkinter as tk

class FallingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Falling Ball")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(180, 20, 220, 60, fill="blue")

        self.velocity = 5  # speed of falling
        self.running = False  # flag for movement

        self.canvas.bind("<Button-1>", self.toggle_movement)

        self.animate()

    def toggle_movement(self, event):
        self.running = not self.running

    def animate(self):
        if self.running:
            self.canvas.move(self.ball, 0, self.velocity)
            x1, y1, x2, y2 = self.canvas.coords(self.ball)
            if y2 > 400:  # reset to top if it goes out of canvas
                self.canvas.coords(self.ball, 180, 20, 220, 60)
        self.root.after(30, self.animate)

# Run the application
w = tk.Tk()

app = FallingBallApp(root)

w.mainloop()
