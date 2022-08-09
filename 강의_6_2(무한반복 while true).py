# 무한반복  while True:
'''
* while True:
    계속 반복

(끄기 : ctrl C)

while True:
    print("녜님")

print("ASDF") -> 안나옴 ^^

* 무한반복을 하다가 어떤 조건에 의해서
반복을 멈출 수 있다!
'''

# break
'''
ex) 정수를 계속 입력 받다가
0 을 입력하면 반복문 종료!

while True:
    s = int(input("정수>"))

    if s == 0:
        break

ex2) 정수를 계속 입력 하다가
0 을 입력하면 반복문 종료
단! 입력한 정수의 합을 출력하세요

total = 0 #입력정수 합 변수

while True:
    s = int(input("정수>"))

    if s == 0:
        break
    
    total += s    

print("총 합:",total)

'''
# 정수를 무한정으로 입력 받다가
# 5의 배수가 5개 입력되면
# 반복문을 종료 프로그램 작성 
'''
count = 0 #개수 변수명

while True:
    s = int(input("정수"))

    if s%5 == 0:
        count +=1

    if count == 5:
        break


'''

'''
count = 0 #개수 변수명

while count != 5:
    s = int(input("정수"))

    if s%5 == 0:
        count +=1
'''
# 구구단 3단 출력 9까지 곱한
# 결과를 출력하세요

# 출력값 :
# 3 * 1 = 3

'''
내가 하려던 식

count = 1
while count != 10:
        print("3","*",count,"=",3*count)
        count += 1
'''

# 답안
'''
d = 1

while d<10:
    print("3 *",d,"=",3*d)
    d +=1
'''


# 2단 부터 9단까지 곱해서
# 결과를 출력하는 프로그램을
# 작성하세요!

'''
g = 1 # 곱하는 수
e = 2 # 단 수

while e < 10:

    while g < 10:
        print(e,"*",g,"=",e*g)
        g +=1
    g = 1 #g 초기화x -> 내부반복 X
    e += 1

아니면


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


#문제!!!
'''
*
**
***
****
*****



   1
  111
 11111
  111
   1


123A
45BC
6DEF


*         *
**       **
***     ***
****   ****
***********



'''





