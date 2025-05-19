import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Falling Ball")

# Create canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create ball
ball = canvas.create_oval(180, 20, 220, 60, fill="blue")

# Movement variables
velocity = 5
running = False

def toggle_movement(event):


    global running
    running = not running

def animate():
    if running:
        canvas.move(ball, 0, velocity)
        _, y1, _, y2 = canvas.coords(ball)
        if y2 > 400:  # Reset to top
            canvas.coords(ball, 180, 20, 220, 60)
    root.after(30, animate)

# Bind click to toggle movement
canvas.bind("<Button-1>", toggle_movement)

# Start animation loop
animate()

# Run the app
root.mainloop()
