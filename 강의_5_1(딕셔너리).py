#딕셔너리 = dict = dictionary
'''
: {}
: 저장방법
-> 변수명 = {key : value}
-> index 없음 = 슬라이싱 불가능!

=> key 자료형 확인
: 중복 X, 변경될 수 있는 자료형 X (리스트X)
: 정수, 문자열, 실수, 튜플 O (고정값)

=> value 자료형 확인 
: 지금까지 배운 자료형 몽땅! 가능!!
: 중복 데이터 허용!

'''
# [] 리스트 (빈 리스트)에 추가를 하려면?
# 함수 append 사용! (맨뒤에 추가)
# 함수 incert 사용! (위치지정가능)
'''
* 딕셔너리는 함수를 사용하지 않아도
변수명[key] = value
-> 추가, 수정, 변경하는 기능!

ex) 가수 그룹의 명수 저장
singer = {"BTS" : 7, "레드벨벳" : 5, "EXO" : 9}

=> 관련 키 : 값 으로 편하게 저장 가능!!

-> 딕셔너리 삭제
: del 변수명[key]

-> key를 이용해서 value 확인
: 변수명[key]

* 딕셔너리 함수

-> keys()
: key값만 따로 뽑아주는 함수 (=리스트 형태로 뽑아줌)
: (리스트 형태에 접근하는 법은 다름!)
=> print(변수명.keys())

-> values()
: values 값만 따로 뽑아주는 함수 
=> print(변수명.values())
: 나온 값에 따로 접근하고 싶다 -> 리스트로 변환해서!
ex)
language = {1: "python",2:"java",3:"C++"}
keylist = language.values()
keylist = list(keylist)
type(keylist)

<class 'list'>
keylist[0]
         
'python'

'''
# keys(),values() 에 접근하서 사용을 하려면
# list 형태로 형을 변환해서 사용해야 한다.

'''
stulist = {"철수":"010-1234-1234",
"영희":"010-2345-2345","혜원":"010-3456-3456"}

일때,

stulist에 혜원이가 있니? 라고 물어볼 때
=> "혜원" in stulist
=> True/False 로 나옴

-> *** in / not in ***
: key 가 딕셔너리 안에 있는지 검사하는 명령어

in/not in
데이터의 유무에 따라 True/False 로
나타나는 명령어
-> list 나 tuple 에도 가능!






















