import random as s

r = s.randrange(1, 101)
t = 0
g = 1
h = 100
while t != r:
    t = int(input("請猜一個數字"))
    if t < r:
        print("在大一點")
    elif t > r:
        print("在小一點")
print("恭喜猜中")