from ttkbootstrap import *
from PIL import Image, ImageTk
import sys
import os

os.chdir(sys.path[0])


def test():
    print("test")


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
button = Button(window, text="瀏覽", command=test, style="my.TButton")
button.grid(row=0, column=2, sticky="W")
button2 = Button(window, text="顯示", command=test, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")

canvas = Canvas(window, width=600, height=600)
canvas.grid(row=2, column=0, columnspan=3, sticky="EW")
window.mainloop()