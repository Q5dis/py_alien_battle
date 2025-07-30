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
        taunt=[
            "자자 착한 지구인아, 제자리로 돌아가라고.",
            "사료재료면 얌전하게 갇혀있을것이지!!",
            f"네 이름이 {value}라고? 지구인들은 원래 그렇게 작명센스가 구린가?",
            "*조롱하듯이 촉수를 흐느적거린다.*"
            "꾸웨에에에에엑! 우리한테 지구말은 다 이렇게 들려."
        ]
        return r.choice(taunt)
    
    def attack():
        attack_damage=r.randint(1,3)
        return attack_damage
    