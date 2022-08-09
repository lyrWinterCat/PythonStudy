# 함수 4가지 종류
'''
=> 입력값이 있느냐/없느냐 반환값이 있느냐/없느냐

* 입력값 0 반환값 0
'''
def getM(a,b):  #매개변수 : 전달되는 값 을 저장

    return a*b
    #return
    #: 함수 종료
    # 결과값을 main 반환
    # return 1개만.
    # 반환하는 데이터는 여러개가 가능.
    # return 뒤에 명령어를 더 써도 작동X


# main : 프로그램이 시작하면 가장 처음
        #호출되서 명령문들을 시작하는 함수

getM(10,10)  #인수 : 함수를 호출할 때
                    #전달하는 입력값을 의미


'''
* 입력값 0 반환값 X
'''
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


