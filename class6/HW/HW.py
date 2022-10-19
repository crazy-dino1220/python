"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""
import turtle as t

t.shape('turtle')
t.penup()
for i in range(0, 360, 45):
    t.left(i)
    t.forward(70)
    t.stamp()
    t.home()
t.done()