while True:
    print("1.加法")
    print("2.減法")
    print("3.乘法")
    print("4.除法")
    op = input("請輸入你想使用的系統的代碼:")
    num1 = input("請輸入第一個數字：")
    num2 = input("請輸入第二個數字：")

    num1 = float(num1)
    num2 = float(num2)

    if op == "1":
        result = num1 + num2
    elif op == "2":
        result = num1 - num2
    elif op == "3":
        result = num1 * num2
    elif op == "4":
        result = num1 / num2
    else:
        print("無效的運算子")

    print("計算結果：", result)