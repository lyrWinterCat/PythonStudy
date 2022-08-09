'''
*형변환
: 데이터의 형태를 변환
ex) 1->"1"
-숫자 1을 문자 1로 변경?
=>str(1)
- 1.1 -> 1 변환?
number = int(1.1)

= 정수를 문자열로 형태를 변환

* str(데이터) : 문자열로 변환
* int(데이터) : 정수로 변환
* float(데이터) : 실수로 변환

ex)
float_number = float(100)
type(float_number); print(float_number)
<class 'float'>
100.0
'''
# 문자열 함수
'''
* upper() : 대문자 변경
사용법 : 변수명.upper()

* lower() : 소문자 변경
사용법 : 변수명.lower()

* replace() : 문자열 치환(변환)
>>> replace_str = str2.replace("PYTHON","Zython")
>>> replace_str
'Zython JAVA C C++

* split() : 문자열 나누기
-> 리스트로 저장을 한다.
>>> str3 = "hello world python"
>>> print(str3.split())
['hello', 'world', 'python']
>>> str3 = "hello/world/python"
>>> print(str3.split("/"))
['hello', 'world', 'python']
'''

# 리스트 == (배열, Arraylist)
'''
-> 여러개의 데이터를 한번에 보관할 수 있는 자료형
-> []
-> 빈 리스트
list1 = []
type(list1)
<class 'list'>

=> 숫자를 여러개 저장?
>>>list2 = [1,2,3,4,5,6,7]
print(list2)
[1, 2, 3, 4, 5, 6, 7]

=> "이서희 20 160.1"
>>>list3 = ["이서희",20,160.1]; print(list3); type(list3)
['이서희', 20, 160.1]
<class 'list'>

- 이서희 -> 강동원 변경
= 수정, 변경, 출력
= 리스트명[index]
--->> list3[0] = "강동원"

- del 리스트명[index]
= 공간/방을 지우고 싶어요

list3    
['강동원', 35, 185.2]
del list3[0] ----> 각각 공간 지움
list3
[35, 185.2]
del list3    ----> 전체 지움
list3
'''
# 리스트 함수 remove()
'''
=> 리스트 연산 (+ , *)

list4 = [1,2,3]
list5 = [4,5,6]
list6,
list7 =
["홍길동", "성춘향", "임꺽정"],[1.1,2.2,3.3]


-> list8 = list4 + list6   ----> 리스트끼리 연결
list8
[1, 2, 3, '홍길동', '성춘향', '임꺽정']
=> 리스트간의 합 : 연결

list5*3 (정수)
[4, 5, 6, 4, 5, 6, 4, 5, 6] ---> 가능 (반복)

list5*list7 ----> 불가능
=> 리스트 * 정수 : 반복

*단, 문자열하고 실수하고는 곱할 수 없다!!
*나눗셈, 뻴셈은 불가능!!


=> 리스트 안에 리스트가 들어가나?
list10 = [1,2,3,["다다","라라"]]
list10[3][0]
'다다'
-> 리스트 안의 리스트 일부 가져오기 ->인덱스사용!
list11 = [[1,2,3],"python"]
list12 = [[1.1,2.2],["java","c++"],"하하"]
'''
# practice = ["I","am","happy","hungry","sing"
# "want","to","sleep","Are","you","?","!"]

# -> 2문장 만들기!

'''
나의 답안
str1 = list13[0],list13[1],list13[2]
str2 = list13[7],list13[8],list13[9]
str1;str2
('I', 'am', 'happy')
('Are', 'you', '?')
'''






































