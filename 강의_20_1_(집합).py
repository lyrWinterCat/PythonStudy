# 집합
# : 순서가 없다.
# : 인덱싱, 슬라이싱 X
# : 중복을 허용하지 않음 !

# 변수명 = set([1,2,3...])

set1 = set([1,2,3])
type(set1)
>>> <class 'set'>

# 튜플이 출력 될 때는 {} 형태
print (set1)
>>> {1, 2, 3}


set3 = set('aabbbbcccc')
set3
{'c', 'a', 'b'}
# : 중복허용 X !!
# : 아무리 같은 문자열이 들어가도
#   하나의 b인 원소만 기억 ! (저장) 

# 교집합 / 차집합 / 합집합


# 교집합 = 공통적인 집합
# 연산자 : & (and)
# A.intersection(B)

ex)
A = set(['a',1,4,'c'])
B = set([1,'c','4',2])
A&B
>>> {1, 'c'}
A.intersection(B)
>>> {1, 'c'}
# : 각각 비교 (정수, 문자, 실수끼리)
# : 동일한 데이터가 있지 않으면 교집합으로 생각 X


# 합집합 = A,B 원소를 모두 갖는 집합
# 연산자 : (shift+\) |
# union 메서드 

A = set(['a',1,4,'c'])
B = set([1,'c','4',2])
A | B
>>> {1, 2, 4, 'c', 'a', '4'}
B.union(A)
>>> {1, 2, 4, 'c', 'a', '4'}


# 차집합 = 중복되는 원소 제거
# 연산자 : -
# difference(데이터)

A = set(['a',1,4,'c'])
B = set([1,'c','4',2])
A-B
>>> {'a', 4}
B-A
>>> {2, '4'}
B.difference(A)
>>> {2, '4'}
# 연산 순서가 데이터를 결정함! 


# 추가 add()

# 여러개 추가 update([1,1,2...])

B.difference_update(데이터)
# : B에 있는 데이터를 수정하세요!


# isdisjoint()
# : 두 집합에 공통적인 원소를 가지고 있니??
# : 결과값 True / False 


# issubset() : 부분집합
# : 결과값 True / False 
A = set(['a',1,4,'c'])
B = set([1,'c','4',2])

{1,'c'}.issubset(B)
>>> True

print(type({1,'c'}))
>>> <class 'set'>

# {} 에서 key 값을 따로 주지 않았다면
# : set 으로 인정 



# canvas 에서 id객체의 좌상담 우하단 좌표
# 반환 메서드 : coords()
# : 현재 객체의 좌표 정보를 얻어옴
# : 리스트 형태

p1 = Airplane(200,400,50,50,can)
x1,y1 = p1.can.coords(p1.id1)
print(x1,"  ",y1)

m1 = Monster(200,200,30,30,can)
xm,ym =m1.can.coords(m1.m1)
print(xm,"  ",ym)



# 연산자 오버로딩
# : 연산자를 객체끼리 사용할 수 있게 하는 기법
# : 어떤 연산자와 함수의 동작을 똑같이 수행하는 메서드를 정의
# __메서드명__(self,other)


# 연산자/함수   메소드     설명
'''
+     __add__(self,other)   덧셈
*     __mul__(self,other)   곱셈
-     __sub__(self,other)   뺄셈
/     __truediv__(self,other)  나눗셈
%     __mod__(self,other)   나머지
<     __it__(self,other)    작다(미만)
<=    __le__(self,other)    작거나 같다(이하)
==    __eq__(self,other)    같다
!=    __ne__(self,other)    같지 않다
>     __gt__(self,other)    크다 (초과)
>=    __ge__(self,other)    크거나 같다(이상)
[index]  __getitem__(self,index)  인덱스 연산자
in    __contains__(self,value)    멤버 확인
len   __len__(self)          요소 길이
str   __str__(self)          문자열 표현
'''

# 두 점 사이의 거리를 구하는 공식
# math.pow(값,지수)
# math.sqrt(a**2 + b**2)  : 제곱


# 몬스터 coords()
# 별 coords()
# 두 점 사이의 거리??

# 몬스터 좌표를 저장?
# 별이 움직일때마다 몬스터의 좌표값을 저장???
# 별이 몬스터를 관리하는 list 를 지워야해??

# 연산 결과를 가지고 0~50? 0~20 범위안에 들어오면 충돌됐다!

# (x,y) (x2,y2)

# 루트 (x2-x1)**+(y2-y1)**











