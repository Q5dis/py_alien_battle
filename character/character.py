import random as r
class DefaultCharacter:
    def __init__(self):
        # 기본정보
        self.name=""

        self.health=10
        self.damage=1
        self.skill=2

        self.select=""

        self.item="" # 아이템은 하나만 장착가능

        self.my_class=""

        self.base_h=self.health
        self.base_d=self.damage
        self.base_s=self.skill

    def attacked(self,value):
        self.health-=value
    
    def attack(self): # 옵션에 따라 데미지를 반환
        if self.select=="1":
            return self.damage
        if self.select=="3":
            taunt=[
                "이 크툴루 짝퉁 외계인 놈들아!",
                "태어나면서 부터 탈모라니 불쌍하군!",
                "점액흘리개 녀석들, 오늘 숙회만들어주마!",
                "라면에 넣고 끓여주마!",
                "우욱... 아 냄시, 아... 아잠깐 냄시... 개심해",
                "너같은거 절대 안 만질거야, 병균옮는다고!",
                "그거 알아? 지구에도 너네 종족 많은거. 근데 개들은 식탁 위에 있지!"
            ]
            return r.choice(taunt)

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
        print(f"      [ {self.my_class} | {self.base_h}/{self.health} | 남은능력:{self.skill} | 아이템[x] ")
    
    def option_selected(self,value):
        if value=="1":
            self.select="1"
        elif value=="2":
            self.select="2"
        elif value=="3":
            self.select="3"
        else:
            self.select="x"