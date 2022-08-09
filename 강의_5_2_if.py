# if~else:
'''
-> 두가지 중 하나를 무조건 실행하는 조건문

else 조건식을 작성할 수 없다!
else는 if 없이 단독으로 사용 불가!!

if~else 는 하나의 세트!  (else는 if의 종속절)



if 조건식 :
    참인경우
    ...

else:
    거짓인 경우
    ...
    


* 나이를 입력 받아서 버스 요금을 계산하는 프로그램
1. 20세 미만이면 무료

'''
age = int(input("나이를 입력>"))
if age<20 : #참인경우
    print("무료")
else: #거짓인경우 
    print("정상요금")
'''

2. 65세 이상 무료!   / 조건이 추가되면...?

: 논리연산자

and 그리고
두 연산이 모두 참일때만 결과가 참!

A연산     B연산      res(결과값)
 true      r=true      true
 T          F           F
 F          T           F

or 또는
두 가지 연산 중 하나만 참이 나오면 결과가 참인 연산!

'''
age1 = int(input("나이를 입력>"))
if age1<20 or age1>=65 : #참인경우
    print("무료")
else: #거짓인경우 
    print("정상요금")




'''
score = int(input("점수입력>"))


점수를 입력 받아서 90 이상이면 수!
                80이상이면 우!
                70 이상이면 미!

if score >=90 :
    print("수")

if score >=80 :
    print("우")

if score >=70 :
    print("미")

print("if문")
'''




'''
res = score >= 60
print(type(res)) # bool

if res : # 조건이 true, false인지 보면됨 
    print("합격")
    print("잘하셨습니다.")

print("if문 끝")
'''
