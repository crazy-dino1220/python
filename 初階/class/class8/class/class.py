# s = int(input("請輸入密碼:"))
# n = 1220
# if s == n:
#     print('密碼正確')
# while s != n:
#     s = int(input("請輸入密碼:"))
#     if s == n:
#         print('密碼正確')
s = int(input("請輸入整數(2以上):"))
i = 2
while s % i == 0 and i != s:
    i += 1
if i == s:
    print('yes')
else:
    print('no')
