# 匯入 tkinter 模組和 random 模組
from tkinter import *
from PIL import Image, ImageTk
import sys
import os


def move_circle(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)
    elif key == "d":
        canvas.move(rect, 10, 0)
    elif key == "a":
        canvas.move(rect, -10, 0)
    elif key == "w":
        canvas.move(rect, 0, -10)
    elif key == "s":
        canvas.move(rect, 0, 10)


def exit_fun():
    windows.destroy()


os.chdir(sys.path[0])
# 創建主視窗
windows = Tk()
windows.title("My first GUI")

quit_btn = Button(windows, text="Quit", command=exit_fun)
quit_btn.pack()

canvas = Canvas(windows, width=500, height=700)
canvas.pack()

windows.iconbitmap("crocodile2.ico")

image = Image.open("uwu.jpg")

img = ImageTk.PhotoImage(image)

my_img = canvas.create_image(300, 300, image=img)

circle = canvas.create_oval(250, 150, 300, 200, fill="red")

rect = canvas.create_text(300,
                          100,
                          text="UWU",
                          fill="black",
                          font=('Arial', 40))

canvas.bind_all('<Key>', move_circle)

windows.mainloop()