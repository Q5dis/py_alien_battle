import character as c
import random as r
# 엘크가 되어 살인
class Elk(c.DefaultCharacter):
    def __init__(self):
        super().__init__()
        self.my_class="엘크"
        # 데미지가 강하지만 인벤토리가 봉인된다.
        self.base_d=5
        self.damage=5

    def attack(self,value):
        if value=="x":
            return "      당신은 엘크라 아이템 사용이 불가능합니다.\n     손을 쓸 수 없어 슬퍼졌습니다..."
        
        elif value=="1":
            print("      # 음무어어어어!!!!!!!!!!!!!")
            print("      # 엘크의 기본공격! 너무 아프다!")
            return self.damage
        
        elif value == "2":
            if self.skill <= 0:
                print("      # 더 이상 박치기를 사용할 수 없습니다!")
                return 0
            self.skill -= 1
            is_succeed = r.randint(1, 101) % 2 == 0
            if is_succeed:
                print("      # 박치기 대성공! 외계인은 즉사했다!!")
                return 99999999
            else:
                print("      # 박치기 대실패... 머리가 조금 아프다...\n      # 체력 -1")
                self.health -= 1
                return 0

        elif self.select=="3":
            taunt=[
                "무어어~~ 무어어어어.",
                "무어어어어!",
                "*화난 엘크 울음소리*",
                "므으으음... 므으음!! 무어어~~",
                "무어어~~ 무우우!!!",
                "무어어~~ 무어~~ 무어어어~~~"
            ]
            return r.choice(taunt)
        return super().attack()

    def info_print(self):
        return """
     목이 마른 당신은 눈앞의 초록색 병을 잡고 꿀꺽꿀꺽 마십니다.
     뭐가 들었는지는 모르겠지만, 설마 죽기야 하겠나요?
     그 때, 뭔가 이상한 일이 벌어집니다.
     머리가 어지럽고, 땅이 점점 멀어지는데...

     유리창에 비친 자신을 보니 영락없는 엘크의 모습입니다.

     ...이건 대체 무슨 물약이었던 것일까요?
     심지어 사람의 목소리도 나오지 않습니다!
     다시 돌아올 수 있는거... 맞겠죠?

     

     당신의 직업은 [ 엘크 ] 포효하는 사슴 입니다.
     캐나다의 숲에서 튀어나온 것 같이 변한 당신...
     어마어마하게 강력한 힘과 공격을 자랑합니다.
              
     당신의 기본 공격력은 아주 강력해졌습니다!
     그러나 신체의 변화로 아이템을 사용할 수 없습니다.
              
     특수공격: 박치기!
     현재 공격중인 적을 강력한 박치기로 즉사시킵니다.
     확률은 되거나 안되거나 둘 중 하나. 실패 시 본인이 1 데미지를 입습니다.
     라운드 중 딱 두 번 사용 가능합니다.
"""