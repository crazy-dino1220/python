s = int(input("請輸入要印出的箭頭大小(奇數)(2~10):"))
import turtle as t

t.shape('turtle')
t.color("blue")
t.penup()
t.left(270)
for i in range(s):
    t.forward(20)
    t.stamp()
t.left(180)
t.forward(s * 20)
t.left(90)
t.stamp()
for i in range((s - 1) // 2):
    t.forward(20)
    t.stamp()
t.left(180)
for i in range(s):
    t.forward(20)
t.left(180)
for i in range((s - 1) // 2):
    t.forward(20)
    t.stamp()
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.stamp()
for i in range((s - 3) // 2):
    t.forward(20)
    t.stamp()
if s == 3:
    t.done
t.left(180)
for i in range(s - 2):
    t.forward(20)
t.left(180)
for i in range((s - 3) // 2):
    t.forward(20)
    t.stamp()
if s == 5:
    t.done
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.stamp()
for i in range((s - 5) // 2):
    t.forward(20)
    t.stamp()
t.left(180)
for i in range(s - 4):
    t.forward(20)
t.left(180)
for i in range((s - 3) // 2):
    t.forward(20)
    t.stamp()
if s < 9:
    t.right(90)
    t.forward(20)
    t.stamp()
    t.done()
t.right(90)
t.forward(20)
t.left(90)
t.stamp()
if s == 7:
    t.done
t.forward(20)
t.stamp()
t.left(180)
t.forward(20 * 2)
t.stamp()
t.left(180)
t.forward(20)
t.right(90)
t.forward(20)
t.stamp()
t.done()
