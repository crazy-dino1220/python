"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""
import turtle as t
import time as s

t.shape('turtle')
for i in range(0, 360, 360 // 60):
    t.right(i)
    t.forward(80)
    s.sleep(1)
    t.home()
    t.clear()

t.done()