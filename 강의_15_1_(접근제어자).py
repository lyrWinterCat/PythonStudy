# 접근제어자
'''
: 접근의 범위를 설정

* 공개 비공개속성
: public = 클래스 안, 밖 모두 접근 가능
: __변수명__ , 변수명
: __메서드명__ , 메서드명 


: private= 클래스 내부에서만 접근 가능
: __변수명, __메서드명 



* private 객체를 생성할때는 초기화 가능 !
'''

# id, pw 저장

class Id:
    def __init__(self,id1,pw):
        self.__pw = pw #밖에서 쉽게접근X, 외부노출 X
        self.id1 = id1

    def info(self):
        print(self.__pw)
        print(self.id1)

# main()
서희 = Id("설난이",1234)
서희.info() # 접근, 호출 가능!
>>>1234
>>>설난이

# main직접호출 =>> 접근X
# AttributeError
print(서희.pw)

#####################################################

# 접근자(getter)와 설정자(setter)
# : private 접근 X, 별도의 메서드 필요
'''
* getter : 인스턴스의 값을 반환할 때 사용

* setter : 인스턴스의 값을 수정/설정/변경할 때 사용
'''

class Id:
    def __init__(self,id1,pw):
        self.__pw = pw #밖에서 쉽게접근X, 외부노출 X
        self.id1 = id1

    def info(self):
        print(self.__pw)
        print(self.id1)

    def getPw(self):
        return self.__pw

    def setPw(self,p):
        self.__pw=p

서희.setPw(6789)
print(서희.getPw())

>>> 6789


#####################################################

# protected
# : 해당 클래스와 그 하위(상속을 받은 자식클래스)만
# 접근 가능
# : 자식클래스 객체를 생성해서만 접근 가능 !
# _변수명

######################################################

















