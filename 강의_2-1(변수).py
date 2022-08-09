'''
변수
* 연산의 결과를 저장하거나 특정 숫자를 기억했다가
내가 원할때마다 가지고 와서 사용하고 싶음*
을 기반으로 하여 나온 개념

-> 데이터를 저장하는 공간
-> 하나의 데이터를 (객체) 저장하는 공간!

-> 객체가 저장된 주소를 가리킴

- 어떻게 만들까?
저장할 공간에 이름을 만들어 주면 됨!
    * 변수명 = 값  /예)  number = 7
    * = (대입연산자)
    * 결합 : 오른쪽 -> 왼쪽

-> 변수 타입 함수
* type(데이터)

-> 변수명
* 숫자로 시작할 수 없음
예) 1num 2n ...
* hello world -> 공백 허용 x
* 공백 혹은 띄어쓰기 : _ (언더바)
* 예약어 사용 X
-> 파이썬에서 지정한 명령문, 함수
(색이 변하는 단어 - 노랑, 자주...)


-> * 예제
- 동물 이름 저장하는 변수
강아지, 고양이, 사자 (단, 한줄에)
animal1, animal2, animal3 = dog, cat, lion
-> 파이썬에서만 가능!

- 한 학생의 이름, 나이, 핸드폰번호, 키

- 이름 : ** 으로 출력하고 싶다면?
print("이름: ", 변수)
-> 이어서 출력 가능!!


-
a = b = c = "사람"
출력했을때 세 문자 모두 사람으로 출력됨

-> 변수 삭제
del 변수명 (메모리에서 삭제)
: print(변수) is not defined

'''
# 실습 1
# 태어난 년도를 저장
# 나이를 계산
# 2021 - 태어난 년도 + 1
# 변수명 birth_year : 태어난 년도
#       age
# 출력 ( 본인 나이 : **)
'''
birth_year = 1995
print(2021 - birth_year + 1)
27
print('본인 나이 : ',2021 - birth_year + 1)
본인 나이 :  27
age = print('본인 나이 : ',2021 - birth_year + 1)
본인 나이 :  27
'''
birth_year = int(input("태어난 년도를 입력하세요"))
age = (2021 - birth_year +1)
print("본인 나이 : ",age,"입니다.")

# 실습 2
# 직사각형의 가로 길이와 세로길이를
#저장하는 변수 면적 계산

#변수명
# width, height - 가로, 세로
# area 면적
# 출력
'''
width = 5
height = 8
area = width*height
'''



