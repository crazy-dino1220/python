try:
    f = float(input('請輸入華氏溫度'))
except:
    print('發生錯誤')
else:
    print("成功執行")
    c = 5 / 9 * (f - 32)
    print('華氏溫度' + str(f) + 'f等於攝氏溫度' + str(c) + 'c')
