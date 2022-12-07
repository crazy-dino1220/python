bag = []
while True:
    print("1.新增餐點")
    print("2.移除餐點")
    print("3.提交菜單")
    ans = input("請輸入功能選項:")
    if ans == "1":
        juices = ['蘋果汁', '柳橙汁', '葡萄汁']
        while True:
            for index in range(len(juices)):
                print(f'{index+1}.{juices[index]}')

            try:
                ans = int(input("請輸入編號:"))
            except:
                print("請輸入數字編號")
            else:
                if ans > len(juices) or ans <= 0:
                    print("輸入錯誤查無此果汁，請重新輸入編號")
                else:
                    bag.append(juices[ans - 1])
                    print(f"您點的商品是{bag}")
                    break

    elif ans == "2":
        r = input("請輸入移除的東西")
        while r in bag:
            bag.remove(r)
        print("移除完成")
        print(f"您點的商品是{bag}")
    elif ans == "3":
        bag2 = []
        for i in bag:
            if not (i in bag2):
                bag2.append(i)
                print(f"{i}={bag.count(i)}")
        print("菜單已提交囉!")
        break

    else:
        print("輸入錯誤")
