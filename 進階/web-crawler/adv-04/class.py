from ttkbootstrap import *
from PIL import Image, ImageTk
from tkinter import filedialog
import sys
import os


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    lable2.config(text=file_path)


def show_image():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),
                         Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo


def test():
    print("test")


os.chdir(sys.path[0])

font_size = 20
window = tk.Tk()
window.title("MY GUI")
window.option_add("*font", ("Helvetica", font_size))
style = Style(theme="vapor")
style.configure('my.TButton', font=('Helvetica', font_size))
lable = Label(window, text="瀏覽檔案:")
lable.grid(row=0, column=0, sticky="E")
lable2 = Label(window, text="無")
lable2.grid(row=0, column=1, sticky="E")
button = Button(window, text="瀏覽", command=open_file, style="my.TButton")
button.grid(row=0, column=2, sticky="W")
button2 = Button(window, text="顯示", command=show_image, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")

canvas = Canvas(window, width=600, height=600)
canvas.grid(row=2, column=0, columnspan=3, sticky="EW")
window.mainloop()