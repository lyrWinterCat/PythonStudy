# 튜플
'''
사용 : 리스트와 똑같음
=> 여러개의 데이터를 동시에 저장
=> ()
=> 데이터값을 수정 및 삭제가 불가능!!!

* 파이썬에서 여러 값을 반환할 때 (한번에)
기본적으로 사용하는 자료형 : 튜플!
'''
# 고정된 튜플값을 변경해서 사용하고 싶을때?
# 형변환 !

'''
튜플 -> 리스트 형변환
list(변수)

리스트 -> 튜플 형변환
tuple(변수)

*튜플 저장시 객체 하나값만 입력할 경우 마지막에
꼭 , 붙여서 저장*

튜플 안에 튜플? 리스트?
-> 가능 ^^
'''

# 예제

# tuple7
([1, 2, 3], 'python', 100.254, (1, 2, 3))
# 리스트 안에 있는 2번 출력은 ?
tuple7[0][1]
# -> 큰 묶음, 작은 묶음의 index 찾아서...

tuple7[0][1]
2
tuple7[0][1] = 10000
tuple7
([1, 10000, 3], 'python', 100.254, (1, 2, 3))
tuple7[1] = 'Zython'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tuple7[1] = 'Zython'
TypeError: 'tuple' object does not support item assignment

# 튜플 안의 리스트값은 변경 가능
# 튜플 안의 튜플 값은 변경 불가능!!

# 예를들어
# 사이트에서 절대 변경 불가능한 값 : ID = 튜플
# 사이트에서 변경 가능한 값 : Password = 리스트


'''
*튜플도 슬라이싱이 될까??  ---> 가능!

tuple2
(1, 2, 1000, 4, 5, 6)
list4 = tuple2[0:3]
list4
(1, 2, 1000)
type(list4)
<class 'tuple'>
list4 = list(tuple2[0:3])
list4
[1, 2, 1000]
type(list4)
<class 'list'>

된다!
단, 형태는 그대로이기 때문에, list로 하고 싶다면
형변환을 시켜주어야 함!

* 인덱스 번호가 부여됨
* 슬라이싱 됨!
* 인덱싱 : 출력, 저장 용도 직접 접근!
'''

# 튜플 연산 : 덧셈, 곱셈 가능!

# 튜플 함수 : count , index 두개만 가능!
'''
* count (데이터) : 개수
-> 데이터의 개수를 반환
: 데이터의 갯수를 보여줌

tuple8 =
("python","Java","Zython","C++","python")

print(tuple8.count("python"))
2

* index(데이터) : 위치 찾기

print(tuple8.index("python"))
0

-> 인덱스 번호를 기준으로 중복이 되는 데이터가
있어도 제일 앞에 있는 데이터의 index 번호를 준다.

-> 중복적인 데이터를 찾으려면??
print(tuple8.index(value,start))

print(tuple8.index("python",1))
4
: 앞선 tuple8에서 0번째에 python 있는 것 확인
따라서 그 다음인 1을 넣어서 순서지점을 정해주면 됨
'''

# 사용자로부터 입력

# 사용자로부터 입력 (키보드)으로 받는 내장 함수
# -> input()

'''
input()
-> 데이터를 문자열로 반환


* 정수 한개를 입력 받겠다.

number = input("정수>")
정수>1000
type(number)
<class 'str'>

number = int(number)
type(number)
<class 'int'>




































































