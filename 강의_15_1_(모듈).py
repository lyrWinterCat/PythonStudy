# sqlite3
'''
: 기본적으로 파이썬에서 데이터베이스를 살짝
맛 볼 수 있는 부분 !

* 파이어베이스  Firebase (강사추천)
=> 파이썬에서 접근가능

# import sqlite3

# 설치 sqlitebrowser.org
# 실행 : SQlite

* DBMS
: 데이터베이스의 역할
: 데이터를 저장하고 운용하는 것 !


* 테이블
: 실제 데이터를 담고있는 것
* 레코드
: 실질적으로 데이터가 담긴 구조표
'''

# sqlite3
'''
가장 먼저 ! 연결 !!
connect  ->  데이터베이스 생성
'''
# dir(참조변수 또는 클래스)
# 그 안의 변수들 탐색
# 문자열로 안에 있는 값을 반환
# 리스트 형태로 메서드, 변수 확인 가능 ! 

import sqlite3
conn = sqlite3.connect('sql_test.db')
print(type(conn))
<class 'sqlite3.Connection'>
print(dir())
['Acc', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__'
 , '__name__', '__package__', '__spec__', 'conn', 'sqlite3', '서희']
print(dir(conn))
['DataError', 'DatabaseError', 'Error', 'IntegrityError'
 , 'InterfaceError', 'InternalError', 'NotSupportedError'
 , 'OperationalError', 'ProgrammingError', 'Warning', '__call__'
 , '__class__', '__delattr__', '__dir__', '__doc__', '__enter__'
 , '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__'
 , '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__'
 , '__lt__', '__module__', '__ne__', '__new__', '__reduce__'
 , '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__'
 , '__str__', '__subclasshook__', 'backup', 'close', 'commit'
 , 'create_aggregate', 'create_collation', 'create_function', 'cursor'
 , 'enable_load_extension', 'execute', 'executemany', 'executescript'
 , 'in_transaction', 'interrupt', 'isolation_level', 'iterdump', 'load_extension'
 , 'rollback', 'row_factory', 'set_authorizer', 'set_progress_handler'
 , 'set_trace_callback', 'text_factory', 'total_changes']

# C드라이브 안에 DBMS 폴더를 만들고, 그 안에 저장 !

# sqlite3 에서 쓰는 자료형들
'''
: 문자열을 저장한다 = text
: float = real
: int = integer
: None = NULL
'''

from sqlite3 import *

# 메모리 DB 접속 (일회성)

con = connect("C:\\DBMS\\Test.db")

# 테이블을 생성
# cursor (데이터 커서) : 데이터베이스 프로그래밍을 하는 동안
#                       사용되는 커서를 생성

cur = con.cursor()

# execute("문자열")

# 생성하기
# cur.execute("CREATE TABLE PhoneBook (Name text,PhoneNum text)")

#데이터 추가하기 (삽입)
cur.execute("INSERT INTO PhoneBook Values('이서희','010-1234-1234')")



con.commit() # 생성된 테이블이나 삽입 데이터를 저장
con.close()

############################################################################


from sqlite3 import *


con = connect("C:\\DBMS\\Person_list.db")
cur = con.cursor()

name = input("이름>>")
age = int(input("나이>>"))
addr = input("주소>>")

# 튜플
cur.execute("INSERT INTO list Values(?,?,?)",(name,age,addr))



#딕셔너리형태로 저장

#cur.execute("CREATE TABLE list(Name text,Age int, Address text)")
#cur.execute("INSERT INTO list Values(:Name,:Age,:Address);"
#            ,{'Name': name,'Age': age ,'Address':addr })


con.commit() 
con.close()

#################################################################################

# 데이터베이스 읽기
'''
: 저장되어있는 테이블의 데이터를 읽는다
: select * from 테이블명 
