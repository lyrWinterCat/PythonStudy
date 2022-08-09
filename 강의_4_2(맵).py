# 예
'''
이름   -> 문자열
나이   -> int
키     -> float
사용자로 부터 입력받아보세요!!

name = input("이름을 입력하세요>")
이름을 입력하세요>이예림
age = int(input("나이를 입력하세요>"))
나이를 입력하세요>20
type(age)
<class 'int'>
hei = float(input("키를 입력하세요>"))
키를 입력하세요>160.15
type(hei)
<class 'float'>

* 변환할 자료형(input(어떤 데이터))
'''
# map()
'''
-> 여러개의 값을 동시에 입력받을 경우 사용!
=> 단! 같은 자료형들로 형변환 할 경우에 사용!!

* map(변환할 자료형,input().split())

map(int,input("숫자를 입력하세요").split(','))
숫자를 입력하세요10,20,30
<map object at 0x00000245A85F6CB0>
=> 앞에 들어갈 공간을 만들어 주어야 함!

num1,num2,num3 = map(int,input("숫자를 입력하세요").split(','))
숫자를 입력하세요10,20,30
num1;num2;num3
10
20
30
-----> 실수

num1,num2,num3 = map(float,input("숫자를 입력하세요").split(','))
숫자를 입력하세요1.1,1.2,1.3
num1;num2;num3
1.1
1.2
1.3
-------> 정수

str1,str2,str3 = input("문자열>").split(' ')
문자열>python java c
str1;str2;str3
'python'
'java'
'c'
-------> 문자열은 그냥 가능~~
'''


