# == 等於
# != 不等於
# <= 小於等於
# >= 大於等於
# < 小於

# and範例 結果(布林)
# False and False False
# False and True False
# True and False False
# True and True True
# or範例 結果(布林)
# False or False False
# False or True True
# True or False True
# True or True True

password = input("請輸入密碼:")
if password == "1255":
    print("看來你又一次矇對了呢")
else:
    print("看來你又忘記密碼了呢，所以我會在一次提示你密碼:125X")
    password = input("請輸入密碼:")
    if password == "1255":
        print("看來你又一次矇對了呢")

    else:
        print("既然又一次猜錯了，那直接告訴你密碼ㄅ:1255")
        password = input("請輸入密碼:")
        if password == "1255":
            print("你終於對了呢")
        else:
            print("stupid bro")
