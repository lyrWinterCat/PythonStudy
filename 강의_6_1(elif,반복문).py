'''
if~elif 여러가지 조건식


if 조건식:
    참인 경우 실행
elif 조건식:
    참인 경우 실행
elif 조건식:
    참인 경우 실행
elif 조건식:
    참인 경우 실행
elif 조건식:
    참인 경우 실행
else:
    거짓일 경우 실행

'''
# 예제1 
# 8세 미만,65세 이상 무료
# 8세 이상 ~ 13세 이하 300원
# 14세 이상 ~ 16세 이하 500원
# 17세 이상 ~ 19세 이하 700원
# 20세 이상 정상요금

'''

age = int(input("나이>"))
if age < 8 or age>=65:
    print("무료")
    
elif age <=13:
    print("300원")

elif age<=16:
    print("500원")

elif age<=19:
    print("700원")

else:
    print("정상요금")
    

'''
# 반복문
'''
: 조건이 true인 동안만
반복문 아래 들여쓰기 된 부분을
반복해서 수행하세요!

* while 조건식:
    참인 경우 실행문장
    ....
    ....

* 반복문 3가지 필요!
1. 초기식 (시작)
2. 조건식 (언제부터 어디까지 반복?,어떤조건에 의해?
            어디까지??)
3. 증감식 (반복문을 끝낼 수 있는 식)
'''
# 1부터 5까지 출력
# 시작 : 1
# 조건 : 5보다 작거나 같을때까지 반복
# 증감 : 증가 1씩
'''
num = 1   #시작

while num <= 5:
    print(num)
    num=num+1

'''
# 10부터 1까지 반복하면서 출력
'''
num1 = 10

while num1 > 0:
    print(num1)
    num1=num1 - 1
'''


# 복합연산자
'''
:   +=   -=   *=   /=
ex) num += 10
: num 변수값과 10 더한다음
  num 변수에 저장하세요!!

'''
#예제
# 1부터 100까지 반복
# 그 중에서 홀수만 출력
'''

number = 1

while number<101:
    if number % 2 == 1:
        print(number)
            
    #print(number)
    number +=2
'''

























    
