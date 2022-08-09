# main 에서 정수 하나를 입력받아서
# showNum() 입력받은 정수를 넘겨준다

# showNum : 전달받은 수~100까지 정수 출력

# 입력 0 반환값 X
def showNum(a):
    for b in range(a,101):
        print(b,end = " ")

#main
number = int(input("정수>"))
showNum(number)
