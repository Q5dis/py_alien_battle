class DefaultCharacter:
    def __init__(self):
        # 기본정보
        self.name=""

        self.health=10
        self.damage=1
        self.skill=2

        self.item="" # 아이템은 하나만 장착가능

        self.my_class=""

        self.base_h=self.health
        self.base_d=self.damage
        self.base_s=self.skill

    def attacked(self,value):
        self.health-=value
    
    def attack(self):
        return self.damage

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
        print(f"      [    1.기본공격  2.특수능력  3.공격회피    ")
        pass
    def status_print(self):
        print(f"      [ {self.my_class} | {self.base_h}/{self.health} | 남은능력:{self.skill} | 아이템[x] ")
    
    def option_selected(self,value):
        if value=="1":
            return 1
        elif value=="2":
            return 2
        elif value=="3":
            return 3
        else:
            return "x"