import random


class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        if damage > self.defense:
            self.health -= damage + self.defense
        return f"{self.name}受到了{damage}點傷害!"


class Mage(Player):
    def __init__(self, name, health, attack, defense, magic_power):
        super().__init__(name, health, attack, defense)
        self.magic_power = magic_power

    def cast_spell(self):
        self.magic_power -= 10
        return self.attack + self.magic_power


class Warrior(Player):
    def __init__(self, name, health, attack, defense, armor):
        super().__init__(name, health, attack, defense)
        self.armor = armor

    def use_armor(self):
        self.health += self.armor


# player1 = Warrior("戰士小明", 100, 15, 10, 5)
# print(f"名稱：{player1.name}")
# print(f"生命值：{player1.health}")
# print(f"攻擊力：{player1.attack}")
# print(f"防禦力：{player1.defense}")

# player2 = Mage("法師小華", 80, 10, 5, 20)
# print(f"名稱：{player2.name}")
# print(f"生命值：{player2.health}")
# print(f"攻擊力：{player2.attack}")
# print(f"防禦力：{player2.defense}")r

# print(player2.take_damage(player1.attack))
# print(f"玩家2血量剩餘:{player2.health}")
# print(player1.use_armor())
# print(f"{player1.name}血量剩餘:{player1.health}")

# print(f"{player2.name}目前魔力:{player2.magic_power}")
# player1.take_damage(player2.cast_spell())
# print(f"{player2.name}對{player1.name}施放魔法攻擊!")
# print(f"{player2.name}目前魔力:{player2.magic_power}")
# print(f"{player1.name}血量剩餘:{player1.health}")
player1 = Warrior(input(print("請填入數據(ex.(戰士小明, 100, 15, 10, 5)):")))
player2 = Mage(input(print("請填入數據(ex.(法師小華, 80, 10, 5, 20)):")))
while True:
    print(player1.name)
