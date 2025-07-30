import random as r
class DefaultCharacter:
    def __init__(self):
        # 기본정보
        self.name=""

        self.health=10
        self.damage=2
        self.skill=2

        self.item="" # 아이템은 하나만 장착가능

        self.my_class=""

        self.base_h=self.health
        self.base_d=self.damage
        self.base_s=self.skill

    def attacked(self,value):
        self.health-=value
    
    def attack(self,value): # 옵션에 따라 데미지를 반환
        if value=="3":
            taunt=[
                "이 크툴루 짝퉁 외계인 놈들아!",
                "태어나면서 부터 탈모라니 불쌍하군!",
                "점액흘리개 녀석들, 오늘 마침내 숙회로 만들어주마!",
                "우욱... 아 냄새, 아... 아 잠깐 냄새...",
                "너같은거 절대 안 만질거야, 병균옮는다고.",
                "그거 알아? 지구에도 너네 종족 많은거. 근데 개들은 식탁 위에 있지!",
                "네 종족 전체를 갈아서 비료로 쓰면 딱이겠네.",
                "저기 벽에 네 뇌수를 발라주고 싶군.",
                "네 머리통을 터뜨려서 무슨 색깔인지 확인해볼까?",
                "오늘 네 살점으로 라면을 끓여주마.",
                "우주 쓰레기처리장에서 나온 실패작 같군.",
                "야, 초장가져와!!!!!!!!!"
                "유언이라도 남겨 봐, 입이라도 있다면 말이지. 아, 너넨 그런거 없지?",
                "네 혈관 속 체액이 무슨 맛일지 궁금하네.",
                "자갈치시장 음식물쓰레기통이 네 엉덩이보다 깨끗하다!",
                "이런 하등한 생명체와 같은 우주를 공유한다니 치욕이야.",
                "네 종족 전체가 지옥에서 썩어 문드러져야 마땅해.",
                "네 시체는 의료폐기물로도 거부당할 거야.",
                "네놈의 내장으로 칵테일이나 만들어야겠다, 그 이름은 니 엄마다!",
                "이 역겨운 생명체야, 존재 자체가 우주의 실수지.",
                "네 종족 전체를 학살하는 게 우주 정화사업이겠네.",
                "네 내장으로 이 우주선 바닥을 장식해주마.",
                "이런 실패작이 어떻게 우주까지 날아왔지?",
                "인간을 실험하겠다고? 진화나 마저 하고 와라.",
                "야, 초장가져와!!!!!!!!!"
                ]
            return r.choice(taunt)
        if value=="x":
            if self.item=="":
                print("      # 사용할 수 있는 아이템이 없습니다. 턴이 낭비되었습니다!")
            elif self.item=="회복물약":
                print("      # 회복물약을 사용했습니다. 체력 모두 회복!")
                self.health=self.base_h
                self.item=""
            elif self.item=="방귀탄":
                print("      # 방귀탄을 사용했습니다.")
                print("      # 현재 적 사망!!!")
                self.item=""
                return 9999999
            elif self.item=="플라즈마폭탄":
                print("      # 플라즈마폭탄을 사용했습니다.")
                print(r"""
    _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    '''--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____
""")
                print("      적이 전멸했습니다... ")
                return "AllDead"


    def levelup(self):
        # 레벨업시 체력 2 증가
        self.health+=2
    
    def damage_up(self,value):
        # 데미지 값 올릴 일 있을때
        self.damage+=value

    def skill_up(self,value):
        # 스킬횟수 올릴 일 있을때
        self.skill+=value

    def reset_to_base(self):
        # 전투 끝나고 시작할 때 값 복원
        self.health = self.base_h
        self.damage = self.base_d
        self.skill = self.base_s

    def info_print(self):
        pass

    def option_select(self):
        print(f"      [    1.기본공격  2.특수능력  3.모욕하기    ")
        pass
    def status_print(self):
        if self.item=="":
            print(f"      [ {self.my_class} | {self.base_h}/{self.health} | 남은능력:{self.skill} | 아이템[x] ")
        else:
            print(f"      [ {self.my_class} | {self.base_h}/{self.health} | 남은능력:{self.skill} | 아이템[{self.item}] ")
    
    def option_selected(self,value):
        if value=="1":
            self.select="1"
        elif value=="2":
            self.select="2"
        elif value=="3":
            self.select="3"
        else:
            self.select="x"