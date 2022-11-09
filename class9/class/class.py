# s = 0
# while s != "4":
#     print('1.頻果汁')
#     print('2.可口可樂')
#     print('3.柳橙汁')
#     print('4.系統關閉')
#     s = input('請輸入你想要的果汁的編號:')
#     if s == "1":
#         print('你選擇了頻果汁，請在25秒內付錢')
#     elif s == "2":
#         print('你選擇了可口可樂，請在25秒內付錢')
#     elif s == "3":
#         print('你選擇了柳橙汁，請在25秒內付錢')
#     elif s == "4":
#         print("系統已關閉")
#         break
#     else:
#         print("輸入錯誤查無此果汁，請重新輸入")
import random as s

r = s.randrange(1, 101)
t = 0
while t != r:
    t = int(input("請猜一個數字"))
    if t < r:
        print("在大一點")
    elif t > r:
        print("在小一點")
print("恭喜猜中")
