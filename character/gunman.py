import character as c
import random as r
# ( -_•)︻デ═一 총으로 살인
class Gunman(c.DefaultCharacter):
    def __init__(self):
        super().__init__()
        self.my_class="건맨"
        self.bullet=8 # 총알을 턴 대신 사용
        self.base_b=self.bullet
    def attack(self, value):
        if value=="1":
            print(f"      # {self.name}님의 기본공격, {self.damage}데미지 공격!")
            return self.damage
        elif value == "2":
            if self.skill <= 0:
                print("      --- 스킬 포인트가 없어 스킬사용이 불가합니다. 턴이 낭비되었습니다.")
                return 0
            self.skill -= 1
            print("      # 빵야! 당신은 [ 연속발사 ] 를 시도했다!")
            is_succeed = r.randint(1, 101) % 2 == 0
            if is_succeed:
                print("      # [ 연속발사 대성공! ] 두 배의 데미지!!")
                return self.damage*2
            else:
                print("      # 연속발사 대실패... 스킬횟수는 성공여부와 상관없이 차감됩니다.")
                return 0
            
    def check_bullet(self):
        return self.bullet
    
    def add_bullet(self,value):
        self.base_b+=value
        self.bullet=self.base_b

    def gun_manager(self):
        on="■"
        on_turn=self.bullet
        off="□"
        off_turn=self.base_b-self.bullet
        print("      [   ",end="")  # 다른 출력과 맞추기 위해 공백 추가
        for i in range(on_turn):
            print(on,end=" ")
        for i in range(off_turn):
            print(off,end=" ")
        print("  ]")
        self.bullet-=1
    
    def info_print(self):
        return """
     당신의 직업은 [ 건맨 ] 발포하는 자 입니다.
     당신의 기본공격과 턴은 총과 총알로 대체됩니다.

     멀리서 싸울 수 있기 때문에 언제나 선공권을 가져갑니다!
     총알은 매 전투가 끝날 때 마다 적의 시체에서 루팅할 수 있습니다.
     앞으로 열심히 예비탄약을 찾아다녀야겠군요.
              
     소지한 총알이 모두 소모될 경우 당신은 즉시 체포당해 사료가 됩니다.
              
     특수공격: 연속 발사!
     하나의 적에게 총알을 두 발 사용하여 두 배의 데미지를 넣습니다.
     이 공격은 성공할 수도 있고, 성공하지 않을 수도 있습니다.
     성공여부와 상관없이 스킬횟수는 차감됩니다.
"""