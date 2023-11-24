import random as r

game = 0
# 定義玩家的物品清單和金錢
inventory = {"antidote": 2}
gold = 100


def fight():
    ft = input(str("請選擇一個數字(一到二):"))
    fit = str(r.randint(1, 2))
    cc = str(r.randint(1, 2))
    print(ft, fit, cc)

    if ft == fit:
        if cc == "1":
            print("你迅速的衝到龍的腹部，並順利的用你鋒利的刀刃畫出了一道紅紅印(攻擊加2)")
            dino.hp -= hero.atk + 2
            if dino.hp < 0:
                game = 1
        elif cc == "2":
            print("就在你快要劃到龍的鱗片時，牠忽然反手賞了你一巴掌(血量-10)")
            hero.hp -= 10

    else:
        print("你到了大草原，但完全找不到龍的蹤影")

    print(dino.name, "血量:", dino.hp)
    print(hero.name, "血量:", hero.hp)


def start():
    print("1.商店")
    print("2.出發屠龍")
    print("3.打工")


class Character:
    def __init__(self, name, hp, atk, defense, gold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.gold = gold


class dino:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense


# 建立角色實例
hero = Character(input("請輸入勇者名稱:"), 100, 30, 10, 100)
dino = dino(input("請輸入魔龍名稱:"), 200, 50, 20)
# 查看角色屬性
print("名稱：", hero.name)
print("生命值：", hero.hp)
print("攻擊力：", hero.atk)
print("防禦力：", hero.defense)
print("金錠", hero.gold)
print("你是將來會是一個偉大屠龍者，你現在的目標是解決這附近的惡龍...")
while True:
    if game == 0:
        start()
        ac = input("請輸入行動代碼:")
        if ac == "1":
            # 定義商店物品清單和價格
            shop_items = {"sword(加30攻擊)": 50, "armor(加30血量)": 100, "shield(加20防禦)": 30}

            # 定義購買物品的函式
            def buy_item(item, cost):
                global gold
                if gold >= cost:
                    if item in inventory:
                        inventory[item] += 1
                    else:
                        inventory[item] = 1
                    gold -= cost
                    print("您購買了", item, "，剩餘金錢為", gold)
                else:
                    print("您的金錢不夠購買此物品。")

            # 顯示商店物品清單
            print("商店物品清單：")
            for item, cost in shop_items.items():
                print(item, " - 價格：", cost)

            # 讓玩家選擇要購買的物品
            item_to_buy = input("請輸入您要購買的物品：")
            if item_to_buy in shop_items:
                buy_item(item_to_buy, shop_items[item_to_buy])
            elif item_to_buy == "sword":
                hero.atk = hero.atk + 30
                print("攻擊:", hero.atk)
                gold = gold - 50
                print("金碇:", gold)
            elif item_to_buy == "armor":
                hero.hp = hero.hp + 30
                print("血量:", hero.hp)
                gold = gold - 100
                print("金碇:", gold)
            elif item_to_buy == "shield":
                hero.defense = hero.defense + 20
                print("防禦:", hero.defense)
                gold = gold - 30
                print("金碇:", gold)
            else:
                print("商店裡沒有這個物品。")

        elif ac == "2":
            fight()
        elif ac == "3":
            wr = input(str("請選擇一個數字(一到二):"))
            wor = str(r.randint(1, 2))
            if wr == wor:
                print("你很優秀，在鐵匠鋪做了一個很好的鋤頭，賺到:50塊金碇!")
                gold += 50
                print("金錠:", gold)
            else:
                print("在鐵匠鋪打工失敗，弄壞了一把鐵劍。")
    else:
        print("GAME OVER")
