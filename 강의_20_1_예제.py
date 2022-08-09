
class op_over:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        self.num += other.num
        return self.num

    def __sub__(self,other):
        self.num -= other.num


a1 = op_over(5)
# other (other.num X 일 경우)
#print(a1 + 5)
#>>>none

b1 = op_over(10)
print(a1+b1)




