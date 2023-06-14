from ttkbootstrap import *
import time


def start_progress():
    for i in range(101):
        progress['value'] = i
        percent_label.config(text=f"{i}%")
        window.update()
        time.sleep(0.05)


window = tk.Tk()
window.title("Progress Bar Example")

progress = Progressbar(window,
                       orient=HORIZONTAL,
                       length=200,
                       mode='determinate')
progress.grid(row=0, column=0, padx=10, pady=10)

percent_label = Label(window, text="")
percent_label.grid(row=0, column=1, padx=10, pady=10)

start_button = Button(window, text="Start", command=start_progress)
start_button.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()