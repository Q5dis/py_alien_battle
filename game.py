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

bat=BattleManager()

is_dead=False
level_now=0
for i in range(5): 
    bat.day_count()
    
    for j in range(15): # 한 라운드는 15턴, 죽거나 턴이 다하면 종료
        if user.health<=0:
            print("사망")
            is_dead=True
            break
        bat.turn_manager()
        user.option_select()
        user.status_print()
        select=input(f"      {user.name}의 선택은? >>> ")
        user.option_selected(select)
        

    if is_dead:
        break

