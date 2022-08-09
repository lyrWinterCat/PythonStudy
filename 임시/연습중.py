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
            raise MyExcept("오류발생")
        
            return print("잔액이 부족합니다")
        else:
            self.balance -= money
            return self.balance
        
class Checking_Account(Account):
    def __init__(self,a,b,c,d):
        self.balance = a
        self.accountNo = b
        self.owerName = c
        self.cardNo = d

    def pay(self,no,money):
        if no != self.cardNo:     
            raise MyExcept("카드번호를 확인하세요")
        elif money > self.balance:
            raise MyExcept("잔액을 확인하세요")
            return self.withdraw(money)

            
        else:
            return self.withdraw(money)

yerim = Checking_Account(190000,1234,"yerim",9876)

try:
    yerim.pay(9876,200000)
    yerim.pay(9870,100000)
    
except MyExcept:
    print("카드번호가 잘못되었습니다.")
print(yerim.balance)
