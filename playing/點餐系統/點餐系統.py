# 定義餐點菜單和價格
menu = {"雞腿飯": 75, "牛肉麵": 85, "蝦仁飯": 95, "排骨飯": 85, "魚排飯": 90, "西瓜汁": 60}

# 讓使用者選擇餐點並加入購物車
shopping_cart = []
while True:
    print(menu)
    print("購物車:", shopping_cart)
    order = input("請輸入餐點（輸入q結束訂購）：")
    if order == "q":
        break
    elif order in menu:
        shopping_cart.append(order)
    else:
        print("無效的餐點")

# 計算總價
total_price = 0
for item in shopping_cart:
    total_price += menu[item]

# 顯示結帳資訊
print("您的餐點：", shopping_cart)
print("總價：", total_price)