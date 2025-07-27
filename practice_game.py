import random
import time

#モンスターリスト
enemy_data = [
    {"name":"スライム", "hp":30, "attack_power":10, "accuracy":80},
    {"name":"ゴブリン", "hp":60, "attack_power":30, "accuracy":65},
    {"name":"ドラゴン", "hp":100, "attack_power":50, "accuracy":50},
]

class Enemy:
    def __init__(self, name, hp, attack_power, accuracy):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.accuracy = accuracy #命中率

    def is_alive(self):
        return self.hp > 0
    
    def attack(self):
        #命中判定
        hit_chance = random.randint(1,100)
        #攻撃命中時、ダメージ計算処理
        if hit_chance <= self.accuracy:
            damage = random.randint(int(self.attack_power * 0.85), self.attack_power) #85%～100%の乱数でダメージ計算
            return damage
        else:
            return 0 #攻撃が当たらなかった
        
class Player:
    def __init__(self, name, hp, attack_power, accuracy):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.accuracy = accuracy
    
    def is_alive(self):
        return self.hp > 0
    
    def attack(self, enemy):
        #命中判定
        hit_chance = random.randint(1,100)
        #攻撃命中時、ダメージ計算処理
        if hit_chance <= self.accuracy:
            damage = random.randint(int(self.attack_power * 0.85), self.attack_power) #85%～100%の乱数でダメージ計算
            enemy.hp -= damage
            print(f"{self.name}の攻撃！{enemy.name}に{damage}のダメージ！")
        else:
            print(f"{self.name}の攻撃！しかし攻撃は当たらなかった……。")
    
    def heal(self):
        heal = random.randint(int(self.attack_power * 0.85), self.attack_power) #85%～100%の乱数で回復計算
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            print(f"{self.name}は回復した！")
        return heal

#プレイヤーの名前を入力
player_name = input("あなたの名前を入力してください。 >> ")
#プレイヤーインスタンス
player = Player(
    name = player_name,
    hp = 100,
    attack_power = 30,
    accuracy = 90
)

#ゲーム開始
print(f"ようこそ、{player.name}さん！")
time.sleep(2)
print("戦闘開始！")

#ランダムで1体選出
chosen = random.choice(enemy_data)

enemy = Enemy(
    name = chosen["name"],
    hp = chosen["hp"],
    attack_power = chosen["attack_power"],
    accuracy = chosen["accuracy"],
)

print(f"{enemy.name}が現れた！")
time.sleep(1)

#バトル処理
while player.is_alive() and enemy.is_alive():
    time.sleep(1)
    print(f"{player.name} HP：{player.hp}")
    time.sleep(1)
    print(f"{player.name}はどうする？")
    time.sleep(0.5)
    cmd = input("コマンドを入力してください。（攻撃/回復/逃げる）>> ")

    #攻撃処理
    if cmd == "攻撃":
        player.attack(enemy)
        time.sleep(1)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            if enemy_damage > 0:
                player.hp -= enemy_damage
                print(f"{enemy.name}の攻撃！{player.name}に{enemy_damage}のダメージ！")
            else:
                print(f"{enemy.name}の攻撃！しかし{player.name}には当たらなかった！")
        else:
            print(f"{enemy.name}は倒れた！勝利！")
            break
    
    #回復処理
    elif cmd == "回復":
        heal_point = player.heal()
        time.sleep(1)
        print(f"{player.name}は{heal_point}回復した！")
        time.sleep(1)
        print(f"{player.name} HP:{player.hp}")
        time.sleep(1)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            if enemy_damage > 0:
                player.hp -= enemy_damage
                print(f"{enemy.name}の攻撃！{player.name}に{enemy_damage}のダメージ！")
            else:
                print(f"{enemy.name}の攻撃！しかし{player.name}には当たらなかった！")
    
    #逃走処理
    elif cmd == "逃げる":
        time.sleep(1)
        print(f"{player.name}は逃げ出した！")
        break

    else:
        print("正しいコマンドを入力してください。")

if not player.is_alive():
    print(f"{player.name}は死んでしまった！")
    print("目の前が真っ暗になった……")