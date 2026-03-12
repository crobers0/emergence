import tkinter as tk

# root
root = tk.Tk(screenName="Emergence", baseName=None, className='Tk', useTk=1)

# canvas
# https://tkdocs.com/tutorial/canvas.html
# canvas = Canvas(parent, width, height, background)
canvas = tk.Canvas(root, width=900, height=600, background="white")
canvas.pack()

# draw
# canvas.create_rectangle(x_topleft, y_topleft, x_bottomright, y_bottomright, fill, outline)
# canvas.create_line(x0, y0, x1, y1)
y = 30
canvas.create_line(0, y, 200, y)

# on left click event
def on_left_click(event):
    x, y = int(event.x), int(event.y)
    canvas.create_rectangle(x-5, y-5, x+5, y+5, fill="black", outline="blue")

# bind left click event
root.bind("<Button-1>", on_left_click)

# start main loop (open window)
root.mainloop()