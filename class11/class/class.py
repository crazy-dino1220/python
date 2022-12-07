b = []
c = []
s = int(input("請輸入背包的大小:"))
for i in range(s):
    t = input("請輸入想裝的東西:")
    b.append(t)
    print(b)

r = input("請輸入想刪除的東西:")
while r in b:
    b.remove(r)
print(b)

bag2 = []
for i in b:
    bag2.append(i)
    print(f'{i}={bag.count(i)}')
