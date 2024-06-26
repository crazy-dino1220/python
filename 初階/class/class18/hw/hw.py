# import modules
from tkinter import *
import os


# user define function
def shutdown():
    return os.system("shutdown /s /t 1")


def restart():
    return os.system("shutdown /r /t 1")


def logout():
    return os.system("shutdown -l")


# tkinter object
master = Tk()

# background set to grey
master.configure(bg='light grey')

# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="play", command=shutdown).grid(row=0)
Button(master, text="restart", command=restart).grid(row=1)
Button(master, text="play hardmode", command=logout).grid(row=2)

mainloop()