# Unit 모듈을 하나 만들어서
# 비행기 틀, 몬스터 틀, 별의 틀
# class 정의해 봅시다 !

from tkinter import *
#from game_main1 import *
from threading import Thread
from time import*
from random import *


class Character:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        print("객체가 생성되었습니다.")
        # 캔버스에 대한 정보(주소) 참조변수 선언!

        # 이미지 클래스..?

class Airplane(Character):
    def __init__(self,x,y,w,h,c):
        super().__init__(x,y,w,h)
        self.can = c        
        self.speedx = 5
        self.speedy = 5
        self.img = PhotoImage(file="fly.png")
        self.id1 = self.can.create_image(self.x
                                         ,self.y
                                         ,image = self.img)
        #print("비행기생성")
        
# 상하좌우로 이미지 이동 

    def move_R(self,event):
        self.can.move(self.id1,5,0)
        self.can.after(1)
        self.can.update()

    def move_L(self,event):
        self.can.move(self.id1,-5,0)
        self.can.after(1)
        self.can.update()

    def move_U(self,event):
        self.can.move(self.id1,0,-5)
        self.can.after(1)
        self.can.update()

    def move_D(self,event):
        self.can.move(self.id1,0,5)
        self.can.after(1)
        self.can.update()

#PhotoImage 클래스
# tkinter 모듈 안에 있는 것 ! 

# 비행기 객체 생성!
#p1 = Airplane(200,400,50,50,can)


# 몬스터 (여러명)
monlist = []

# 몬스터 생성 시간?
# 쓰레드 실행시 상속받아서 실행

class Monster(Character):
    def __init__(self,x,y,w,h,c):
        super().__init__(x,y,w,h)
        self.can = c
        self.img2 = PhotoImage(file="mon.png")
        self.m1 = self.can.create_image(self.x
                                         ,self.y
                                         ,image = self.img2)

        print("몬스터 생성")
    

class MyThread_Mon(Thread):
    def __init__(self,can):
        Thread.__init__(self)
        self.can=can

    def run(self):
        while True:
            x = randrange(300)
            y = randrange(300)
            monlist.append(Monster(x,y,30,30,self.can))
            sleep(0.5)
        



# 별 (스페이스키를 누르면 계속 생성)
# 인스턴스를 저장하는 리스트
# 별 클래스를 생성하는 스레드 작성

starlist = []

class Star(Character):
    def __init__(self,x,y,w,h,c):
        super().__init__(x,y,w,h)
        self.can = c
        self.img3 = PhotoImage(file="star.png")
        self.s1 = self.can.create_image(self.x
                                         ,self.y
                                         ,image = self.img3)
        print("별 생성")

#key를 누르면 계속 생성 
    def move_up(self,event):
        while self.y > 0:
            self.y -=5
            self.can.move(self.s1,0,-5)
            self.can.after(20)
            self.can.update()
            
            x1,y1 = self.can.coords(self.s1)
            print(x1,y1)

            if y1 < 10:
                del self.s1
                self.can.update()


            
       
class MyStar(Thread):
    def __init__(self,c):
        Thread.__init__(self)
        self.can=c
        self.daemon = True

    def info(self):
        starlist.append(Star(18_Game_main1.px1.x
                             ,18_Game_main1.px1.y
                             ,30,30,self.can))
        #18_Game_main1.px1.x 그대로 못가지고옴 

    def run(self):
        while True:
            self.info()
            sleep(0.5)

