import time as t
import random as r
from character import *
from enemy import *

class TextPrint():
    def __init__(self):
        pass
    def text_print(self,text):
        for line in text.split('\n'):
            print(line)
            t.sleep(0.1)

text=TextPrint()
text.text_print(
"""
.·*¨`*·.·*¨`*·.·*¨`*·..·*¨`*·.·*¨`*·.·*¨`*·.
      
당신은 평범한 지구인이었다...
... 그랬어야만 했다.
      
그러나 이제 당신은 평범한 지구인이 아니다...
왜냐하면 당신은 현재 우꿀꿀루 종족의 외계함선으로 납치당했기 때문이다...
      
하지만 당신은 가만히 앉아서 실험을 당하거나 사료가 되진 않을것이다

당신은...

싸울 것이다...
      
이 몸이 얼마나 으스러지든...

저 망할 촉수쟁이들에게 본때를 보여주겠어!!!!!!!

아... 그리고 참고로...
아이템 사용 키는...
.
.

"x"
.
.

니까...

잊지 말도록 하자...?
꼭...!!
      
.·*¨`*·.·*¨`*·.·*¨`*·..·*¨`*·.·*¨`*·.·*¨`*·.
""")

print("이 촉수쟁이 녀석들은 내 진짜이름을 알 필요가 없어.")
name= input("전투에서 사용할 당신의 이름을 입력하세요: ")
print(f"\n     {name}... \n     이순신의 기상이 느껴지는군요...")

text.text_print("     \n     그런 당신의 눈 앞에는 세개의 물체가 놓여있습니다.\n     전류가 흐르는 삼단봉,\n     낙지가 꿈틀거리는 총,\n     ...그리고 초록색, 그리고 분홍색 물약.\n     무엇을 선택하시겠습니까?")
t.sleep(0.5)
print("     \n     (숫자로 선택해주세요.)\n     1. 삼단봉\n     2. 낙지총\n     3. 초록색 물약\n     4. 분홍색 물약 (주의! 이 옵션은 게임의 장르를 바꿔버립니다!)\n")
temp=input(f"     {name}의 선택은...: ")

if temp=="1":
    user=Smacker()
    user.name=name
    text.text_print(user.info_print())
    t.sleep(1)
elif temp=="2":
    user=Gunman()
    user.name=name
    text.text_print(user.info_print())
    t.sleep(1)
elif temp=="3":
    user=Elk()
    user.name=name
    text.text_print(user.info_print())
    t.sleep(1)
elif temp=="4":
    user=Seducer()
    user.name=name
    text.text_print(user.info_print())
    t.sleep(1)
else:
   classes = [Smacker(), Gunman(), Elk()]
   print("     !! 에라 모르겠다, 당신은 운명에 몸을 맏깁니다...\n") # 랜덤선택
   user = r.choice(classes)
   user.name = name
   text.text_print(user.info_print())
   t.sleep(1)

bat=BattleManager()
is_dead = False
level_now = 0

for i in range(5):  # 5일간 전투
    bat.day_count()
    user.reset_to_base()
    if bat.day==2 or bat.day==4:
        print("     & 레벨업! 능력치가 상승되었습니다!! ")
        print("        체력 +2     기본데미지 +1")
        user.levelup()
        if user.my_class=="스매커":
            print("     & 스매커의 특수능력으로 기본데미지가 두배가 되었습니다. ")
            print("                현재 데미지 두배!!")
            user.twice_damage()
    # 적 생성 (day, 즉 레벨에 따라 다른 적 배치)
    if bat.day <= 2:
        enem = Lv_1()
    elif bat.day == 3:
        enem = Lv_3()
    elif bat.day == 4:
        enem = Lv_4()
    else:
        enem = Lv_Boss()
        text.text_print("""
     드디어 도착한 우주선의 함장실.
                        
     그런데 저건...
        ... 사람의 실루엣? 
    
     어떻게 된거지?...
        ... 당신은 가까이 다가갔다...
                        
    그러나 당신을 반기는 것은 인간이 아니었다...
    피부는 짙은 초록색으로 녹아버렸고
    한쪽 팔은 기계와 촉수가 섞인 무언가였다.
                        
    오래 전에 인간이길 포기한, 그 자...
                        
    그자의 이름은...
    
    [  보스 이안  ]...
    
    그 역시 당신처럼 함선에 납치된 시민이었다.
    그러나 이제 그는 외계인의 모습으로
    지구인들을 가차없이 학살하는 괴물이 되어있었다...

    '... 어리석은 속셈은 집어치우시지, 인간.'          
""")

    for j in range(15):  # 15턴
        if user.health <= 0:
            print("사망")
            is_dead = True
            break
        if enem.health <= 0:
            print(f"      !! {enem.name} 사망")
            break
        elif enem.health <=0 and bat.day==5:
            t.sleep(0.5)
            print("      드디어 당신은 보스를 처치했다...!!")
            t.sleep(0.5)
            print("      입에서 초록색 피를 흘리는 두목이 당신에게 무언가 말한다...")
            t.sleep(0.5)
            print("      ....")
            t.sleep(0.5)
            print("      ....")
            t.sleep(0.5)
            print("      ....")
            t.sleep(0.5)
            print("      ....")
            t.sleep(0.5)
            print("      ' 매일 프로그래머스 문제 하나씩 푸세요 '")
            t.sleep(0.5)
            print("      ------- 게임 클리어!! -------")
        
        print("\n")
        bat.turn_manager() # 턴 수 출력
        user.status_print() # 스탯 출력
        user.option_select() # 옵션 출력

        if user.my_class == "건맨":
            # 건맨이 먼저 공격
            select = input(f"      # {user.name}의 선택은? >>> ")
            damage_to_enemy = user.attack(select)
            if isinstance(damage_to_enemy, int):
                t.sleep(0.5)
                enem.attacked(damage_to_enemy)
                t.sleep(0.5)
            if enem.health > 0:
                t.sleep(0.5)
                damage_to_user = enem.attack(user.name)
                t.sleep(0.5)
                user.health -= damage_to_user
                t.sleep(0.5)
                print(f"      # - {user.name}님은 {damage_to_user}만큼 피해! 현재 체력: {user.health}\n")
                t.sleep(0.5)

        else:
            # 적이 먼저 공격
            t.sleep(0.5)
            print(f"      > {enem.taunt(user.name)}")
            t.sleep(0.5)
            damage_to_user = enem.attack(user.name)
            user.health -= damage_to_user
            t.sleep(0.5)
            print(f"      > - {user.name}님은 {damage_to_user}만큼 피해! 현재 체력: {user.health}\n")
            
            if user.health <= 0:
                is_dead = True
                break

            select = input(f"      # {user.name}의 선택은? >>> ")
            if select !="x":
                t.sleep(0.5)
                damage_to_enemy = user.attack(select) # 유저의 공격값을 저장
                t.sleep(0.5)
                enem.attacked(damage_to_enemy) # 그 값을 토대로 공격당함.
            print("")

            if isinstance(damage_to_enemy, str):
                t.sleep(0.5)
                print("      # - 당신은 외계인의 눈 앞에서 모욕한다.")
                t.sleep(0.5)
                print(f"      # - {damage_to_enemy}\n")  
                t.sleep(0.5)
                print(f"      # - 별 효과는 없지만 외계인은 화가났다.\n")  

            print(" _________________________________________________________ ")
        if is_dead:
            break
    if is_dead:
        t.sleep(0.5)
        print("     -- 아아... 눈이 감긴다... 이게... 죽음인가?_")
        t.sleep(0.5)
        print("      -- 당신의 여정은 이 곳에서 끝이 납니다....")
        t.sleep(0.5)
        print("      -- 게임 오버! 당신의 시체는 사료가 되었습니다. --")
        break
    # 전투 성공 후 아이템 처리 등
    if user.my_class != "엘크":
        print("      ------- 전투 성공 -------")
        print("      이제 시체를 루팅하자.")
        is_picked = bat.item_picking()
        if is_picked:
            print("      > 아이템을 장착하시겠습니까? 이전에 장착한 아이템이 있다면 교체됩니다.")
            a = input("(y/n): ")
            if a == "y":
                user.item = bat.picked_item
                print("      성공적으로 장착되었습니다.")
            elif a == "n":
                print("      아이템이 유지되었습니다.")
            else:
                user.item = ""
                print("      의사표현이 확실하지 않아 현재 가진 아이템도 소멸되었습니다.")
