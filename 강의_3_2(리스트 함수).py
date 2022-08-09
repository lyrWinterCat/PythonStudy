#3-1 예제
# practice = ["I", "am", "happy","hungry","sing",
# "want","to","sleep","Are","you","?","!"]
# 2문장
'''

* 리스트 슬라이싱
=> 리스트명[시작:끝]
list1 = ["python","java","c","c++"]
list2 = list1[0:2]
list2
['python', 'java']
list2[0] = "Zython"
list2
['Zython', 'java']
list3 = list1[1:]
list3
['java', 'c', 'c++']
'''
# 3-2 예제
'''
str3 = "201906111014"
슬라이싱을 이용해서
2019년 -> year
06월 -> month
11일 -> day
10시 , 14분 -> 각각 변수

그 변수들을 이용해서

2019년 06월 11일 10시 14분 입니다.
라고 출력
=> 문자열은 변경x, 슬라이싱을 이용해서 변경!

***내 답
year = str3[0:4],"년"
month = str3[4:6],"월"
day = str3[6:8],"일"
time = str3[8:10],"시"
minite = str3[10:],"분"
nd = "입니다."

print(year);print(month);print(day);
print(time);print(minite);print(nd)
('2019', '년')
('06', '월')
('11', '일')
('10', '시')
('14', '분')
입니다.
'''
# 진호 첨삭 받은 식
'''
year = str3[0:4]+"년"
year
'2019년'
month = str3[4:6]+"월"
day = str3[6:8]+"일"
hour = str3[8:10]+"시"
minite = str3[10:]+"분"
print(year,month,day,hour,minite,nd)
2019년 06월 11일 10시 14분 입니다.
'''



#파이썬 역순으로 데이터를 출력, 변경 가능
# - 값으로 index 번호를 지정할 수 있다.
# 단! -0 은 없음! -1부터 시작!

'''
0~ 시작 : 왼쪽 -> 오른쪽
-1 시작 : 오른쪽 -> 왼쪽
'''

# 리스트 안에 리스트 슬라이싱??
# -> 해봐야 함
'''
* 슬라이싱은 많이 해봐야 늘음!!!
'''
# 빈 리스트에 "python" 저장
'''
list1 = []
list[0] = "python"
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list[0] = "python"
TypeError: 'type' object does not support item assignment

-> 빈리스트에 데이터를 추가할 때는 함수가 필요!
'''
# append(데이터) : 추가 
# 맨 뒤에 저장한 요소들이 추가된다.
'''
list1 = []
list1.append("python")
list1
['python']
list1.append(1)
list1.append(1.1)
list1
['python', 1, 1.1]
list1.append(['이서희','이지희'])
list1
['python', 1, 1.1, ['이서희', '이지희']]
list1.append(4,5,6) -> 불가능!!
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    list1.append(4,5,6)
TypeError: list.append() takes exactly one argument (3 given)
'''
# insert(index,value) : 삽입
'''
list3 = [1,2,3,4,5,6,7]
2와 3사이?
list3.insert(1,1000)
list3
[1, 1000, 2, 3, 4, 5, 6, 7]
???
list3 = [1,2,3,4,5,6,7]
list3.insert(2,1000)
list3
[1, 2, 1000, 3, 4, 5, 6, 7]
'''

# remove(value) : 값을 지우는 함수
list3
[1, 2, 1000, 3, 4, 5, 6, 7]
list3.remove(1000)
list3
[1, 2, 3, 4, 5, 6, 7]
list3.remove(4)
list3
[1, 2, 3, 5, 6, 7]
'''
중복값이라면 앞에 먼저 위치한 값부터 지움
'''
# -> 없는 데이터가 있으면 valueError 오류를 띄어줌
'''
=> del 과 remove ?
index 번호를 가지고 지우느냐/값을 가지고 지우느냐 차이
'''
# pop(index) : 위치에 있는 데이터를 지우는 함수
'''
-> 삭제되는 데이터를 보여준다!!




=> run module 이나 F5 누르면 오류남 ^^
'''




