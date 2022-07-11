import tkinter as tk
from time import strftime
from tkinter.ttk import *

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def help ():
    label1 = tk.Label(root, text= "help = Displays commands currently usable, dir = Shows available directories, files = Shows available files,", text2 =  "run = Runs an executable file, end = Ends code, settings = Shows settings for EYN-DOS, install = Searches for installables. Attempting to execute an unkown command results in a blank response. For further support, contact EYN-DOS Support#9295 via Discord or eyndos@gmail.com via electronic mail.", fg='black', font=('Ariel', 12))
    canvas1.create_window(150, 200, window=label1)


menu = tk.Button(root, width = 5, height = 1, fg = 'black', text='Menu', command = help)
menu.pack(side = 'top')

blank1 = tk.Label(root, width = 5, height = 1, text='')
blank1.pack(side = 'top')
    
shut_down = tk.Button(root, width = 8, height = 1, fg = 'black', text='Shut Down')
shut_down.pack(side = 'bottom')

blank2 = tk.Label(root, width = 5, height = 1, text='')
blank2.pack(side = 'bottom')

test1 = tk.Button(root, width = 8, height = 1, fg = 'black', text='test')
test1.pack(side = 'left')

test1 = tk.Button(root, width = 8, height = 1, fg = 'black', text='test')
test1.pack(side = 'left')

test1 = tk.Button(root, width = 8, height = 1, fg = 'black', text='test')
test1.pack(side = 'left')

test1 = tk.Button(root, width = 8, height = 1, fg = 'black', text='test')
test1.pack(side = 'left')

test1 = tk.Button(root, width = 8, height = 1, fg = 'black', text='test')
test1.pack(side = 'left')

test1 = tk.Button(root, width = 8, height = 1, fg = 'black', text='test')
test1.pack(side = 'left')

test1 = tk.Button(root, width = 8, height = 1, fg = 'black', text='test')
test1.pack(side = 'left')

def time():
    string = strftime('%H:%M %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl= Label(root, font = ('ariel', 13),
            background = 'white',
            foreground = 'black')
lbl.pack(side = 'top')
time()

root.mainloop()