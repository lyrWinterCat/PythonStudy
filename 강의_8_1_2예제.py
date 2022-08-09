'''
# 세개의 수를 받아서
# 가장 큰 수를 main에서 출력
# 결과값을 돌려주는 함수

def funt1(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

    
res =funt1(1,2,3)
print("가장큰 값 :",res)

print("가장 큰 값:",funt1(2,3,4))

'''

# 예금계좌
# 계좌번호 , 잔액

# 입금할 때?
# 돈 입금 후 돌려주는것X
# 그냥 통장에 저장

def deposit(a):
    print(a,"입금했습니다.")


# 출금
# 출금액 입력 -> 출금 확인 -> 돈을 돌려줌 

def withdraw(b):
    money = 10000
    if b > money:
        return "잔액이 부족합니다."
    else:
        return b
#잔액조회 
def account_Check():
    print("잔액조회창입니다.") 
    
#main

print("*"*15)
print(" ATM 기계입니다.")
print("1. 입금.")
print("2. 출금")
print("3. 잔액조회")
print("4. 종료") 
print("*"*15)

sel = int(input(">"))
if sel ==1:
    deposit(10000)

elif sel==2:
    res =withdraw(9000)
    print("출금액:",res)

elif sel ==3:
    #잔액조회
    account_Check()

elif sel==4:
    print("ATM 종료")

else:
    print("선택 오류") 






