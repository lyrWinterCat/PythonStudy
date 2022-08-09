# 자동차 클래스
# Car
# 브랜드명, 가격, 속력, 색상
# 기능 X (함수 따로 안넣어요)

# 현대 소나타
# 4000
# 240
# 검은색

# Benz S클래스
# 1억
# 300
# 하얀색

# 각각의 인스턴스를 생성해서 모든 정보를
# 출력!

# 두 차를 모두 구입했을 경우의 가격 출력
# 총 가격:** 입니다.

class Car:
    brand = 0 #쌤: Brand_name=""
    price = 0
    speed = 0
    color = 0 #  : color=""
    
# 정보출력 메서드
# : 클래스 안에 포함되어있는 함수 = 메서드
    def info(self):
        print("*"*10)
        print(self.brand)
        print(self.price)
        print(self.speed)
        print(self.color)
        print("*"*10)
    
a = Car()
a.brand = "현대 소나타"
a.price = 4000
a.speed = 240
a.color = "검은색"

b = Car()
b.brand = "Benz S클래스"
b.price = 10000
b.speed = 300
b.color = "하얀색"

a.info()
b.info()


print(a.brand,a.price,a.speed,a.color,sep='\n')
print(b.brand,b.price,b.speed,b.color,sep='\n')

print("*"*15)

print("총 가격 : "+str(b.price+a.price)+"만 원 입니다.")


