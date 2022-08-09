# 점치는 프로그램
# 당신의 고민
# 당신의 이름?
# 입력


# 랜덤클래스
# 임의의 수를 하나 뽑아주는 모듈(파일)
# import random
# 랜덤클래스 정보를 포함

# 정수를 뽑는 내장함수
# randint(시작,끝)
'''
randint(1,10)
-> 1에서 10까지중 랜덤으로 하나!
'''
'''
import random

name = input("이름>")
q = input("고민을 입력>")
print(name,"님의 고민>",q)

print("잠시 기다리세요//")

print("점치는 중....")

s = random.randint(1,5)

if s == 1:
    print("백프로 확신합니다.")
elif s == 2:
    print("노력하면 될껄?")
elif s == 3:
    print("신력이 떨어졌다..")
    print("다음에 다시오세요")

elif s == 4:
    print("죽기전엔 될껄??")

else:
    print("믿으면 된다.")
'''

import random

name = input("이름>")
q = input("고민을 입력>")
print(name,"님의 고민>",q)

print("잠시 기다리세요//")

print("점치는 중....")

s = random.randint(1,5)

list1 = ["백프로확신"
         ,"노력하면 될껄?"
         ,"신력떨어짐"
         ,"죽기전엔될껄"
         ,"믿으면 된다."]
print(list1[s-1]) #인덱스번호. 0부터시작 고려!
# 5를 index값으로 주면 에러!!

if s == 1:
    print("백프로 확신합니다.")
elif s == 2:
    print("노력하면 될껄?")
elif s == 3:
    print("신력이 떨어졌다..")
    print("다음에 다시오세요")

elif s == 4:
    print("죽기전엔 될껄??")

else:
    print("믿으면 된다.")
