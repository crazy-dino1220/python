from tkinter import *


def hi_fun():
    global change
    print("hahahahahahahahaha")
    if change == False:
        display.config(text="babababababababababa", fg="red", bg="blue")
    else:
        display.config(text="babababababababababa", fg="red", bg="blue")


win = Tk()
win.title("my first GUI")  #設定視窗名稱
btn = Button(win, text="Click me", command=hi_fun, fg="#555DBA", bg="#B0EFBA")
btn.pack()

display = Label(win, text="hi", fg="#B0EFBA", bg="#B0AD3D")
display.pack()

win.mainloop()  #保留視窗
