from ttkbootstrap import *
from PIL import Image, ImageTk
from tkinter import filedialog
import sys
import os


def on_switch_change():
    print("test")


os.chdir(sys.path[0])

font_size = 20
window = tk.Tk()
window.title("MY GUI")
window.option_add("*font", ("Helvetica", font_size))
style = Style(theme="vapor")
style.configure('my.TButton', font=('Helvetica', font_size))

check_type = BooleanVar()
check_type.set(True)

check_label = Label(window, text="True")
check_label.grid(row=1, column=2)

check = Checkbutton(window,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change)
check.grid(row=1, column=1)

window.mainloop()