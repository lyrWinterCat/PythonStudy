# 오버라이딩 
'''
: 부모로 부터 받은 메서드 내용을
자식클래스에 맞게 내용을 변경하는 것 !

: 재정의 한다.!

* 오버라이딩 조건
: 메서드명 동일
(: 매개변수 개수는 보지 않음 ! )


* 부모한테 받은 메서드보다 우선적으로 호출됨 !
'''

# 예시
class Animal:
    def __init__(self,name):
        self.name = name

    def cry(self):
        pass
    


class Puppy(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def cry(self):
        print("멍멍")


class Cat(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def cry(self,str1):
        print(self.name, str1)

고양이 = Cat("초코",2)
고양이.cry("야옹야옹")

강아지 = Puppy("뽀삐",1)
강아지.cry()


# 좌표클래스

# x,y 좌표저장

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def draw(self):
        print("x>",self.x)
        print("y>",self.y)

    
# x,y,z

class Point3D(Point):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

        
    # 메서드 오버라이딩 
    def draw(self):
        print("x>",self.x
              , "y>",self.y
              , "z>",self.z)


c1 = Point3D(10,10,10)
c1.draw()

# 자식클래스가 부모클래스를 호출하고 싶을 경우?
# super()

#   메서드super().부모클래스내용

# x,y,z 예시 다시 

class Point3D(Point):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

        
    # 메서드 오버라이딩 
    def draw(self):
    # 부모클래스 호출!! 
       super().draw()
       print("z>",self.z)


c1 = Point3D(10,10,10)
c1.draw()

# 부모클래스 생성자 호출은??
# 부모의 객체를 생성하는 방법:

#   MRO
# : 파이썬에서 클래스 탐색 순서를 알려주는 아이

#  객체지향언어 기본적 object 클래스
# 자동적으로 상속받음 

class A:
    def __init__(self):
        print("a") 

class B(A):
    def __init__(self):
        print("b")

class C(B):
    def __init__(self):
        print("c")

c1 = C()

#상속의 순서를 보고싶은데... c만 나옴

print(C.mro())

# [<class '__main__.C'>, <class '__main__.B'>
# ,<class '__main__.A'>, <class 'object'>]

# + 
class C(B):
    def __init__(self):
        super().__init__() #부모생성자 호출
        print("c")



# 총정리
class A:
    def __init__(self):
        print("a") 

class B(A):
    def __init__(self):
        super().__init__()
        print("b")

class C(B):
    def __init__(self):
        super().__init__() #부모생성자 호출
        print("c")

c1 = C()

#상속의 순서를 보고싶은데... c만 나옴

print(C.mro())

# [<class '__main__.C'>, <class '__main__.B'>
# ,<class '__main__.A'>, <class 'object'>]


# 부모클래스에서 객체생성을 할 때 
class A:
    def __init__(self,a):
        self.a = a
        print("a") 

class B(A):
    def __init__(self):
        super().__init__(10) # 값을 주어야함
        print("b")

class C(B):
    def __init__(self):
        super().__init__() 
        print("c")

#또다른예제
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("부모")


    def draw(self):
        pass


class Rect(Shape):
    def __init__(self,x,y):
        super().__init__(x,y) #super()
        print("사각형")

    #오버라이딩
    def draw(self):
        print("사각형 그린다.")
        print("가로>",self.x)
        print("세로>",self.y)

r1=Rect(10,10)
r1.draw()

# 부모
# 사각형
# 사각형 그린다.
# 가로> 10
# 세로> 10
#######################################################

# 클래스 변수, 클래스 메서드
'''
 : 공유변수 , 공유 메서드
 : 공유 폴더 같은 개념
 : 클래스 변수는 모든 인스턴스가 공유
 : 인스턴스가 생성되기 이전에 이미 메모리 공간에 상주!
'''

# 접근하는 방법
# : 객체를 생성하지 않아도 접근 가능 !! 


# 클래스 메서드
'''
: 인스턴스가 생성되기 이전에 메모리 공간에 먼저 할당(선언)
접근 :
=> 클래스명.메서드 형태
@classmethod

'''


# 인스턴스 메서드
'''
: 클래스 생성 후 메인(main)에서 객체를 (인스턴스를) 생성할때
메모리공간에 선언됨

접근:
=> 인스턴스명.메서드()
'''


class B:
    # 클래스 변수 (공유되는 변수)
    int1=0


    # 클래스 메서드,인스턴스메서드
    # def 메서드명():
    #       인스턴스변수! (각각 들어가는 변수)

print(B.int1)
>>>0

b1=B()

print(b1.int1)
print(B.int1)
>>>0
>>>0

b1.int1=1000 #클래스변수x #새로운 인스턴스변수O

print(b1.int1)
print(B.int1)

>>>1000
>>>0 #클래스접근 

#########################################################
# 계좌번호
# 은행에서 부여~

class Account:
    count = 1 # 공유
    count_number = 1111 # 공유

    def __init__(self,money):
        self.money = money
        print(Account.count,"번 고객님 계좌",
              Account.count_number)
        Account.count +=1
        Account.count_number +=1


        
        
a1=Account(10000)
b1=Account(1000)

>>> 1 번 고객님 계좌 1111
>>> 2 번 고객님 계좌 1112

###########################################################
class Account:
    count = 1 # 공유
    count_number = 1111 # 공유

    def __init__(self,money):
        self.money = money
        print(Account.count,"번 고객님 계좌",
              Account.count_number)
        Account.count +=1
        Account.count_number +=1
        self.count = 100
        print("자신count>",self.count)
        self.count+=1     
        
a1=Account(10000)
b1=Account(1000)

print(a1.count)
print(b1.count)


>>> 1 번 고객님 계좌 1111
>>> 자신count> 100
>>> 2 번 고객님 계좌 1112
>>> 자신count> 100
>>> 101
>>> 101




