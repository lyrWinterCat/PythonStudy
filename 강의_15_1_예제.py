
class Acc:
    publicVar = "공개"
    __privateVar = "비공개"
    def __init__(self):
        self.__money = 100000

    def __privateMethod(self):
        print("비공개")

서희 = Acc()
서희.__privateMethod

try:
    print(Acc.__privateVar)
    print(Acc.publicVar)
    
except AttributeError:
    print("접근불가")


#서희.money = 10
#print(서희.__money) 
