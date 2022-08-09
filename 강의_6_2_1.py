# 구구단 3단 출력 9까지 곱한
# 결과를 출력하세요

# 출력값 :
# 3 * 1 = 3

'''
count = 0
while count != 9:
    a = int(input("정수>"))

    if int(0<a<10):
        print("3","*",a,"=")
        count += 1

'''

d = 1

while d<10:
    print("3 *",d,"=",3*d)
    d +=1

# 2단 부터 9단까지 곱해서
# 결과를 출력하는 프로그램을
# 작성하세요!

g = 1 # 곱하는 수
e = 2 # 단 수

while e < 10:

    while g < 10:
        print(e,"*",g,"=",e*g)
        g +=1
    g = 1 #g 초기화x -> 내부반복 X
    e += 1

아니면

'''
#g = 1
e = 2

while d<10:
    g = 1
    while g<10:
        print(d,"*",g,"=",d*g)
        g += 1
    d += 1

'''
# 이런 식으로 g를 안에 넣어주는 것도 방법! 













