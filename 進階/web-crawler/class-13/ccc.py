from ttkbootstrap import *
from lol.lol import *


def get_video_info_gui():
    _, _, _, _, res = get_video_info(lon_entry.get())
    res_option['menu'].delete(0, 'end')
    for r in res:
        res_option['menu'].add_command(label=r, command=tk._setit(res_var, r))

    res_var.set(res[0])


def download_video_gui():
    if download_video(lon_entry.get(), res_var.get()):
        icon_label.config(taxt="下載完成")

    else:
        icon_label.config(text="解析度錯誤")


font_size = 20
window = tk.Tk()
window.title("YouTubew")
window.option_add("*font", ("Helvetica", font_size))
style = Style(theme="minty")
style.configure('my.TButton', font=('Helvetica', font_size))
style.configure('my.TCheckbutton', font=('Helvetica', font_size))
icon_label = Label(window, text="請輸入youtube網址")
icon_label.grid(row=0, column=0)
lon_entry = Entry(
    window,
    width=20,
)
lon_entry.grid(
    row=0,
    column=1,
)
search_button = Button(window,
                       text="獲得影片資訊",
                       style='my.TButton',
                       command=get_video_info_gui)
search_button.grid(
    row=0,
    column=2,
)
search_button = Button(window,
                       text="下載影片",
                       style='my.TButton',
                       command=download_video_gui)
search_button.grid(
    row=1,
    column=2,
)
icon_label = Label(window, text="選擇影片解析度")
icon_label.grid(row=1, column=0)
icon_label = Label(window, text="")
icon_label.grid(row=2, column=0)

res_var = tk.StringVar()
res_option = OptionMenu(window, res_var, ())
res_option.grid(row=1, column=1)
window.mainloop()