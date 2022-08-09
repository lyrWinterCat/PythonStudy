# game_main 모듈
# 비행기 객체들이나 몬스터, 별에
# 객체를 생성해서 (인스턴스 생성)

# 윈도우 창을 만들고, Canvas 생성 

# 모듈 정리

from tkinter import *
from Unit1 import *
from time import *
from random import *

win = Tk()
can = Canvas(win,width=400,height=600,bg='black')
can.pack()

# 비행기 객체 생성!
p1 = Airplane(200,400,50,50,can)
can.create_image(p1.x,p1.y,image = p1.img)

win.mainloop()
