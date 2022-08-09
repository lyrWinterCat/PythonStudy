#가변인자 *매개변수
'''
def nameShow(*a):
    print(a)

nameShow("이서희")
nameShow("이서희","이지희")
nameShow("다다",20,"010-1234-1234")
'''

# 매개변수자리 초기화설정
'''
def nameShow(a="무명씨"):
    print(a)

nameShow()

nameShow("라라") 
'''

# 한명의 정보를 받아서 출력
# 초기값 설정시 항상 뒤에서부터 작성!!

'''
def say_myself(name,age=0,man=True):
    print("나의 이름:",name)
    print("나의 나이:",age)

    if man:
        print("남자")
    else:
        print("여자")
say_myself("라라",10,False)
say_myself("설난",12,)
say_myself("미미")
'''


#가변인자 + 초기값설정
# fun3의 1이 a1에 걸림
# 나머지가 가변인자에 걸림 
'''
def fun3(a1="무명",*a2):
    print(a1)

    for i in a2:
        print(i , " 수")

fun3(1,2,3,4,5)
'''


# 가변인자가 앞에 오면?  =>에러 
# 몇개까지 가변인자가 받아야 하는지 이해 X
# : 오류!!/여러개를 받아서 구별 X
'''
def fun3(*a2,a3):
    for i in a2:
        print(i , " 수")
    print(a3)

    
fun3(1,2,3,4,5)
'''




        







