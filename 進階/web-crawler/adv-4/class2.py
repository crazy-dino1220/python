from ttkbootstrap import *
from PIL import Image, ImageTk
from tkinter import filedialog
import sys
import os


def test():
    print("test")


os.chdir(sys.path[0])


def show_result():
    entry_text = entry.get()
    b = eval(entry_text)
    lable.config(text=b)


font_size = 20
window = tk.Tk()
window.title("MY GUI")
window.option_add("*font", ("Helvetica", font_size))

style = Style(theme="vapor")
style.configure('my.TButton', font=('Helvetica', font_size))
entry = Entry(window, width=30)
entry.grid(row=0, columnspan=2, padx=10, pady=10)
button = Button(window, text="顯示計算結果", command=show_result, style="my.TButton")
button.grid(row=4, column=0, columnspan=2, sticky="N", padx=10, pady=10)
lable = Label(window, text="顯示結果")
lable.grid(row=5, column=0, columnspan=2, sticky="N", padx=10, pady=10)

window.mainloop()