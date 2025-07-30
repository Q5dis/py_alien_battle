import character as c
# ( -_•)︻デ═一 총으로 살인
class Gunman(c.DefaultCharacter):
    def __init__(self):
        super().__init__()
        self.my_class="건맨"
        self.bullet=8 # 총알을 턴 대신 사용
        self.base_b=self.bullet

    def check_bullet(self):
        return self.bullet
    
    def add_bullet(self,value):
        self.base_b+=value
        self.bullet=self.base_b
    
    def info_print(self):
        return """
     당신의 직업은 [ 건맨 ] 발포하는 자 입니다.
     당신의 기본공격과 턴은 총과 총알로 대체됩니다.

     멀리서 싸울 수 있기 때문에 언제나 선공권을 가져갑니다!
     총알은 매 전투가 끝날 때 마다 적의 시체에서 루팅할 수 있습니다.
     앞으로 열심히 예비탄약을 찾아다녀야겠군요.
              
     소지한 총알이 모두 소모될 경우 당신은 즉시 체포당해 사료가 됩니다.
              
     특수공격: 연속 발사!
     하나의 적에게 총알을 두 발 사용하여 끝장 낼 수도 있고,
     하나의 적+그 다음 적에게 연속으로 공격데미지를 넣을 수도 있습니다.
     라운드 중 딱 두 번 사용 가능합니다.
"""