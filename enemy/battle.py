import random as r
import time as t
from character import *


class BattleManager():
    def __init__(self):
        self.enemy_amount=0
        self.turn=15
        self.day=0
        self.location=["함선 입구","식료품 관리실","외계 거주구역","비밀 실험실","두목의 방"]
        pass

    def set_enemy_amount(self,amount):
        self.enemy_amount=amount
        return self.enemy_amount

    def day_count(self):
        print(f"""
     _______________________________________

        하루가 지났다 ... Day {self.day+1}: {self.location[self.day]}
     _______________________________________
""")
        self.day+=1
        self.turn=15
        

    def turn_manager(self):
        on="■"
        on_turn=self.turn
        off="□"
        off_turn=15-self.turn
        print("      [   ",end="")
        for i in range(on_turn):
            print(on,end=" ")
        for i in range(off_turn):
            print(off,end=" ")
        print("  ]")
        self.turn-=1
    
    def item_picking(self):
        for i in range(3):
            t.sleep(0.5)
            print("\n      뒤적...")
            t.sleep(0.3)
            print("")
        item_list=["회복물약","방귀탄","플라즈마폭탄"]
        item_picked=r.choice(item_list)
        
        drop_or_not=r.randint(1,101)

        if drop_or_not%2==0:
            print(f"      >> 획득한 아이템: {item_picked}!")
        else:
            print("       >> 아무것도 나오지 않았다...")



class LoveManager(BattleManager):
    def __init__(self):
        super().__init__()

class GunmanManager(BattleManager):
    def __init__(self):
        pass