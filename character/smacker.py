import character as c
# 외계삼단봉
class Smacker(c.DefaultCharacter):
    def __init__(self):
        super().__init__()
        self.my_class="스매커"
    
    def twice_damage(self):
        # 레벨업 할 때 마다 데미지가 두배로 강해짐
        self.base_d*=2
        self.damage=self.base_d

    def info_print(self):
        return """
     당신은 눈 앞에 보이는 가장 기본적인 무기를 집습니다.
     짜릿한 전류가 흐르는 이 삼단봉...
     가벼우면서도 단단한 재질입니다. 외계의 기술이네요.
     함선 내에서 말썽을 부리는 이들을 제압하는 용도 같군요.
     아마 먼저 발견하지 않았더라면 이 봉으로 맞았을 지도 모릅니다.
              
     

     당신의 직업은 [ 스매커 ] 후려치는 자 입니다.
     당신의 공격력은 레벨업 할 때 마다 두배가 됩니다!
              
     특수공격: 연속감전!
     현재 공격중인 적에게 추가 2 데미지를 주고 뒤에 대기중인
     적에게 최대 5의 데미지를 넣습니다.
     라운드 중 딱 두 번 사용 가능합니다.
"""
