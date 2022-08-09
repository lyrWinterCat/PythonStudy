# 계좌클래스
# accountNo : string
# ownerName: String
# balance : int

# deposit : 입금
# withdraw : 출금 -> 잔액이 부족합니다. 예외발생!

# Checking_Account
# cardNo : string
# pay() : 카드번호,잔액이 부족하면 예외 발생!


#예외처리하는 클래스
class MyExcept(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return value


class Account:
    def __init__(self,a,o,b):
        self.accountNo = a
        self.ownerName = o
        self.balance = b

    def deposit(self,money):
        self.balance += money
        print("잔액>",self.balance)

    def withdraw(self,money):
        if (money > self.balance):
            return print("잔액이 부족합니다")
        else:
            return self.balance -= money
        
class Checking_Account(Account):
    def __init__(self,a,b,c,d):
        self.balance = a
        self.accountNo = b
        self.owerName = c
        self.cardNo = d

    def pay(no,money):
        if :
            print("카드번호 or 잔액 확인하세요")

        else:
            return withdraw(money)
            #withdraw(money)
    
#main()
# raise 내가 만든 예외(메시지)
# 돈이부족/카드번호x/...상황에 맞게 ! 

seohee = Checking_Account()



#결제를 하는데 돈이 부족, 카드 번호 X 예외 
seohee.pay()


#출금하는데 돈이 부족하다 예외 
seohee.withdraw()

# 정상적으로 실행될 수 있도록 코딩하기

##################################################################

# 재고관리 클래스

# StockManager 클래스명
# stockNum :재고수량
# subStock : 재고 수량을 파악해서 수량보다 많으면 예외 발생!
#   "재고 부족!" 예외출력

class StockManager:
    def __init__(self,s):
        self.stockNum = s

    def substock(self,amount):
        if(amount > self.stockNum):
            print("재고부족")

        else:
            print("남은 재고")
            return self.stockNum -= amount

#main()
#예외처리클래스

try:

except:



















