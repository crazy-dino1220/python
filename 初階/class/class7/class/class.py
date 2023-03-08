# import turtle as t
# t.tracer(1, 0)
# for i in range(99999):
#     t.fillcolor('yellow')
#     t.pensize(10)
#     t.pencolor("yellow")
#     t.begin_fill()
#     for i in range(5):
#         t.forward(130)
#         t.left(144)
#     t.end_fill()

#     t.fillcolor('blue')
#     t.pensize(10)
#     t.pencolor("blue")
#     t.begin_fill()
#     for i in range(5):
#         t.forward(130)
#         t.left(144)
#     t.end_fill()
# t.done()
try:
    n = int(input('請入一個整數:'))
    s = 0
    for i in range(1, n + 1):
        s = s + i
    print(s)
except:
    print("錯誤")
finally:
    print('程式結束')