# 계좌번호
# 은행에서 부여~

class Account:
    count = 1 # 공유
    count_number = 1111 # 공유

    def __init__(self,money):
        self.money = money
        print(Account.count,"번 고객님 계좌",
              Account.count_number)
        Account.count +=1
        Account.count_number +=1
        self.count = 100
        print("자신count>",self.count)
        self.count+=1     
        
a1=Account(10000)
b1=Account(1000)

print(a1.count)
print(b1.count)
