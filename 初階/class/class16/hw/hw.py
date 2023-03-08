import turtle as t


def tree():
    x = int(input('請輸入X座標:'))
    y = int(input('請輸入Y座標:'))
    t.speed(1000)
    t.goto(x, y)

    t.done()


tree()