
# 모듈 추가하는 공간
from tkinter import*
from random import*
from time import*

# 함수
def onClick(event):
    print("키보드>",event.keycode)

    
# 클래스
# 공 클래스를 생성할 때 랜덤색상을 지정
color = ['red','blue','yellow','pink','green','orange']

class Ball:
    def __init__(self,x,y,can):
        self.x=x
        self.y=y
        self.color = choice(color)
        self.can=can
        self.ball = self.can.create_oval(self.x,self.y
                                         ,50,50,fill=self.color)
        print("볼생성")

    #이동할때 메서드
    def move_left(self,event):
        can.move(self.ball,-5,0)
        can.after(10)
        can.update()

    def move_right(self,event):
        can.move(self.ball,5,0)
        can.after(10)
        can.update()
        
#애니메이션

win  = Tk()
can = Canvas(win,width=400,height=400)
can.pack()

b1 = Ball(10,10,can)

can.bind("<Left>",b1.move_left)
can.bind("<Right>",b1.move_right)
can.focus_set()


win.mainloop()
