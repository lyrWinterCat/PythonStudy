'''
#생성자 예제

class A:
    #빈 클래스
    #기본생성자
    def __init__(self):
        pass #(숨어있음)
        

        
    pass

A()
'''

# 생성자를 이용해서 인스턴스 변수 생성
# 계좌명,계좌번호,잔액
# 비밀번호

# 입금, 출금, 예금조회

''''
class Account:
    def __init__(self,name,num,money,pw):
        self.acc_name = name
        self.acc_num = num
        self.acc_balance = money
        self.acc_pw = pw
        print("계좌등록 ok")

    # 입력값 O 반환값 O 
    # 출금 
    def with1(self,money):
        if money <= self.acc_balance:
            self.acc_balance -=money
            return money

        else:
            return "잔액 부족"

    # 입력값 O  반환값 X
    # 입금
    def posit(self,money):
        self.acc_balance += money
        print("입금액:",money)

# 영희 철수 지수 계좌생성 
영희 = Account("영희계좌","1111",10000,1234)
print(영희.acc_name)


영희.posit(20000)
영희.with1(5000)
print("출금:",영희.with1(50000))

'''
# 생성자 / 소멸자
'''
class B:
    def __init__(self):
        print("객체 생성")

    def __del__(self):
        print("객체 소멸")
        # 할 게 없다면 pass 써도 됨


b1 = B() # 객체 생성됐다

del b1   # del 이용해서 지우면 "객체 소멸" 출력
         # pass : 아무것도 출력 X 

'''

# 상속 연습
# 평균 클래스
# 평균을 내는 기능

# 총점 클래스
# 총점을 저장하는 변수
# 총점을 계산하는 기능
'''
class Avg:
    def __init__(self):
        self.avg = 0
        
    def average(self,total):
        self.avg = self.total / 3
        print("평균<",self.avg)

class Total(Avg):

    def total(self,kor,math,eng):
        self.kor = kor
        self.math = math
        self.eng = eng
        self.total = kor + math + eng


        self.average(self.total)

person1 = Total()
person1.total(92,92,92)

'''

# 교수, 어린이, 학생
# -> 사람 -> 행동/ 먹고 놀고 자고 (기능)

# 기본 클래스 (부모클래스)

'''
class Person:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job

    def eat(self):
        print(self.name+"님이 먹는다\.")

    def sleep(self):
        print(self.name+"님이 잔다\.")

    def play(self):
        print(self.name+"님이 논다\.")

    def __del(self):
        print("객체가 소멸합니다\.") 

class Child(Person):
    pass

class Student(Person):
    pass

class Professor(Person):
    pass
'''

# 신용카드

#놀이동산 50%
#영화 몇회 무료
#쇼핑 30% 할인
#교통카드

class Trans_card:
    pass    # 교통카드

class Shopping:
    pass    # 쇼핑 할인

class Movie:
    pass    # 영화 무료 

class Park: # 놀이동산
    pass

class Card:
    def __init__(self,name,pw,number):
        self.name=name
        self.pw=pw
        self.number=number
        print("카드 생성 완료")

    def pay(self):
        print("결제합니다.")
    
# 다중 상속
# 클래스들끼리 여러개를 상속 받을 수 있다!!
# class 클래스명(상.클1,상.클2,....)


#삼성카드 -> 쇼핑, 교통 기능!
class Samsung_Card(Card,Shopping,trans_Card):
    pass
#롯데카드 -> 영화
class Lotte_Card(Card,movie):
    pass

#KB카드 -> 결제
class KB_Card(Card):
    pass






























