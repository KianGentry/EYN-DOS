import tkinter as tk
from tkinter import *

root= tk.Tk()

root.title("Mouse detector")

canvas=tk.Canvas(root, width=500, height=500)
canvas.pack()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    canvas.create_window(500,500)

root.bind('<Motion>', motion)
root.mainloop()

