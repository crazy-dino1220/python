import random as r

cat = {"health": 100, "hunger": 0, "happiness": 100}


# 定義玩家的功能
def feed():
    if cat["hunger"] >= 10:
        cat["hunger"] -= 10
        print("您的貓吃了飯，飢餓值減少 10，目前飢餓值為", cat["hunger"])
    else:
        print("您的貓已經吃飽了，無需再喂食")


def play():
    if cat["happiness"] <= 90:
        cat["happiness"] += 10
        print("您和貓玩了一會兒，快樂值增加 10，目前快樂值為", cat["happiness"])
    else:
        print("您的貓已經很快樂了，無需再玩")


def heal():
    if cat["health"] <= 90:
        cat["health"] += 10
        print("您的貓去看病了，健康值增加 10，目前健康值為", cat["health"])
    else:
        print("您的貓已經很健康了，無需再看病")


while True:
    sss = r.randint(1, 5)
    if sss == 1:
        print('你與貓咪玩耍中...')
    elif sss == 2:
        print("貓咪吃飯耶到...")
    elif sss == 3:
        print("貓咪很無聊...")
    elif sss == 4:
        print("你帶貓咪去散步...")
    else:
        print("天上忽然掉下了一個蘋果...")

    if sss == 1:
        print('貓咪玩累了，飢餓值+15')
        cat["hunger"] += 15
    elif sss == 2:
        print("貓咪吃飯耶到，血量-8")
        cat["health"] -= 8
    elif sss == 3:
        print("貓咪很無聊，快樂-10")
        cat["happiness"] -= 10
    elif sss == 4:
        print("貓咪撞到電線杆，血量-20")
        cat["health"] -= 20
    else:
        print("貓咪吃了天上掉下了一個蘋果，飢餓-20、血量+25")
        cat["health"] += 25
        cat["hunger"] -= 20

    print("貓咪狀態:", cat)
    print("1.餵食")
    print("2.玩耍")
    print("3.看醫生")
    ac = input('請輸入行動代碼:')
    if ac == "1":
        feed()
    elif ac == "2":
        play()
    elif ac == "3":
        heal()

    if cat["hunger"] >= 50:
        print("貓咪餓死了...")
        break
    elif cat["health"] <= 0:
        print("貓咪被你害死了")
        break
    elif cat["happiness"] <= 20:
        print("你必沒有給予貓咪太多的關愛，貓咪離家出走了")
        break
