s = int(input("請輸入開始的整數:"))
n = int(input("請輸入結束的整數:"))

for x in range(s, n):
    i = 2
    while x % i != 0 and i != x:
        i += 1
    if i == x:
        print(x)
