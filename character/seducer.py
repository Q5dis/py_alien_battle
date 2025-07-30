import character as c
# 외계인 유혹자
class Seducer(c.DefaultCharacter):
    def __init__(self):
        super().__init__()
        self.my_class="세듀서"
        self.charm=1
        self.base_c=self.charm

    def set_charm(self,value):
        # 모든 종류의 공격이 막힘
        # 유혹능력치 조정
        self.base_c+=value
        self.charm=self.base_c
    
    def reset_to_base(self):
        self.charm=self.base_c
        return super().reset_to_base()
        

    def info_print(self):
        return """
     눈 앞엔 다양하고 강력한 무기들이 있지만
     어쩐지 당신은 화려한 분홍색의 액체에 눈길이 갑니다.
     
     당신은 포션의 목을 쥐고 상지구인처럼 테이블에 내리칩니다
     그리고 남은 액체를 온 몸에 뿌리고 핥아먹습니다!
    
     그러자... 따듯한 기운이 몸을 감싸고...
     ...어쩐지... 나른한 기분이 드네요.
              
     

     당신의 직업은 [ 세듀서 ] 유혹하는 자입니다.
     외계인에게 달콤한 약속을 속삭이며 모두 그대의 편으로 만드세요
              
     이제 당신의 목적은 더이상 살인이 아닙니다...
     이 우주선을 사랑의 요람으로 재구성 하는 것이죠.
              
     모든 종류의 공격이 봉인되고 새로운 옵션들이 생깁니다!
     함선의 모든 외계인들을 유혹해보세요.
              
     특수능력: 낙지... 좋아하세요?
     라운드 한번 당 외계인의 사랑스러운 촉수에 입을 맞출 수 있습니다.
     외계인은 입맞춤을 받으면 즉시 사랑의 노예가 되어 전투불능상태가 됩니다.
"""

    def option_select(self):
        print(f"      [    1.달콤한말  2.특수능력  3.모욕하기    ")
