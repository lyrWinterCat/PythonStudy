#mod2.py

# 모듈을 실행할 파일

#import mod1 as a #모듈명에 새로운 이름을 붙여줄래
# 모듈 불러오기 


# from mod1 import int_a,string_b,함수명,클래스명 ( ()X )
# import include
# 모듈 1 안에서 int_a 만 포함할거야. (모듈 안에 포함시킴)

from mod1 import *



#실질적으로 모듈안으로 들어가서
# 변수, 함수를 호출해줘야 함!!
print(int_a)
# print(int_a) => 값만 정상적으로 나옴
# 나머지 프린트값에 a. 나 mod1. 값을 다 지우면
# 출력오류 남 


print(string_b)
print(list_c)

# 데이터 변경!!
# 3->1000

int_a=1000
print(int_a)


#함수호출
module_test()
module_test2(10)

# 클래스
서희 = Calc()     # 인스턴스 (각각이 소유)
철수 = Calc()     # 인스턴스

서희.mul(10,10)
철수.add(5,5)

'''
ex)
커피= 객체
~의 커피 = 인스턴스

스마트폰 = 객체
~의 핸드폰 = 인스턴스

계산기 = 객체
~의 계산기 = 인스턴스

: 각각이 가지고 있는 것이 인스턴스
: 통칭적으로 보는 것이 객체
'''

# 모듈 이름 쓰는 것이 너무 귀찮아..
# -> 이름을 줄이는 방법? : 별명붙이기













