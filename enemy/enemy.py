import random as r
class Enemy:
    def __init__(self):
        # 기본정보
        self.name=""
        self.health=5
        self.damage=1
        self.power_attack=0

        self.love=3

    def taunt(value):
        taunt_list=[
            "다리 두개 달린 괴물녀석, 썰어주마!",
            "사료재료면 얌전하게 갇혀있을것이지!!",
            f"네 이름이 {value}라고? 그런 멍청한 이름은 처음듣는다!",
            "촉수의 매운 맛을 보여주마!",
            "이 "
        ]
    def attack():
        attack_damage=r.randint(1,3)
        return attack_damage
    