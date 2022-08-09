# game_main 모듈
# 비행기 객체들이나 몬스터, 별에
# 객체를 생성해서 (인스턴스 생성)

# 윈도우 창을 만들고, Canvas 생성 

# 모듈 정리

from tkinter import *
from Unit1 import *
from time import *
from random import *


def funt1(event):
    # 별의 객체를 생성하는 쓰레드를 실행 

win = Tk()
can = Canvas(win,width=400,height=600,bg='black')
can.pack()

# 비행기 객체 생성!
p1 = Airplane(200,400,50,50,can)

m1 = Monster(200,200,30,30,can)

s1 = Star(p1.x,p1.y,30,30,can)

#t1 = MyThread_Mon(can)
#t1.start()

can.bind("<Left>",p1.move_L)
can.bind("<Right>",p1.move_R)
can.bind("<Up>",p1.move_U)
can.bind("<Down>",p1.move_D)
can.bind("<space>",funt1)



can.focus_set()
win.mainloop()


'''
#몬스터 관리
monlist = []

#몬스터 객체 생성
m1 = Monster(100,100,30,30,can)

for i in range(5):
    x = randrange(300)
    y = randrange(400)

    monlist.append(Monster(x,y,30,30,can))
    print(monlist[i].x,monlist[i].y)

for i in range(5):
    can.create_image(monlist[i].x
                     ,monlist[i].y
                     ,image = monlist[i].img2)

# 좌우상하 방향키를 누르면 그림을 이동 !
'''
