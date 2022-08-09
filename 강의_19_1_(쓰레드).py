# 쓰레드 (스레드)  ((=채팅프로그램))
# threading 모듈

# Thread 클래스를 상속 받아서 사용


# run()
# : 스레드가 실행할 때 수행해야 되는 
#   명령문들의 집합

# : 자식클래스를 생성하면 start()
#   호출을 하며 자동적으로 run() 실행


# 싱글 스레드
# : 순차적으로 실행 코드

# ThreadEx (싱글)


# main 스레드
# : 파이썬 프로그램이 시작하고 나서
# 명령문들을 실행하는 함수

'''
from time import*

#from threading import*
from threading import Thread

def my():
    for i in range(3):
        print("I'm Thread")
        sleep(1)

my()

for i in range(3):
    print("I'm main")
    sleep(0.5)

print("end")
'''

#멀티 스레드
'''
from time import*

#from threading import*
from threading import Thread

def my(val):
    for i in range(3):
        print("I'm Thread")
        sleep(1)
        
# run() 없이
# Thread(첫번째 스레드 함수 이름,
#   매개변수를 튜플형태로 전달)

t1 = Thread(target=my,args=(1,))

# Thread 인스턴스 안에 start()
t1.start()



for i in range(3):
    print("I'm main")
    sleep(0.5)

print("end")
# 다른 스레드가 끝날때까지 기다린다.
# t1 main에서 실행하는 쓰레드
# t1.스레드가 끝날때까지 기다린다.
t1.join()
'''
# 데몬쓰레드
# 메인 프로그램이 종료 될 때
# 자동으로 같이 종료된다.



# 다른 모듈 import 시 중복 문제 해결
# if __name__== "__main__":
# 











