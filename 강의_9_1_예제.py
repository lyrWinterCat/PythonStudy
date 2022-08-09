
class Animal:
    age = 0
    name = 0

    def cry(self,str1):
        print(self.name,str1,"한다.")

#main

a = Animal()


# a주소를 이용해서 Animal 객체에
# 토끼, 3살임을 저장.
a.name = "토끼"
a.age = 3

print(a.age)
print(a.name)

b = Animal()
b.name = "강아지"
b.age = 1

print(b.name)
print(b.age)

#하나의 객체에 토끼, 강아지 동시 저장?
#리스트 사용!

Animallist = [] #빈리스트

Animallist.append(a)
Animallist.append(b)

print(Animallist)


# id(데이터) 내장함수
# : 내가 생성한 class의 주소값을 보고 싶을때
# : 객체의 주소를 반환하는 함수
# print(id(a))












