# 그림판 복습 


'''
from tkinter import*

win  = Tk()
can = Canvas(win,width=400,height=400) #bg='black'이면
까만 배경화면 가능 


#사각형 그림을 가지고 있는 can
# 사각형 그리기
#create_rectangle(시작하는 x,y좌표,끝나는 x,y,좌표)


can.create_rectangle(50,50,200,200,fill='blue')
can.pack()

win.mainloop()
'''
#choice([데이터1,데이터2,....])
# 리스트 자료형에서 임의의 값을 반환

#randrange(시작,끝-1)
# 시작, 끝-1 사이의 숫자 무작의 출력
# randrange(0,10,2)
# : 0이상 10미만 중 2의 배수를 반환

# sample()
# 로또 1~45 중복x
# sample(range(1,46),6)
#: 1부터45까지의 숫자 중 6개를 중복없이 뽑아줘!
#: 자료형을 인자로 전달받아서 임의의 값을
# 필요한 개수만큼 리스트로 반환 
# 중복 제거!!!

#-------------> 반환값 O

# shuffle()
# 전달받은 자료형 내용을 임의의 순서대로 (랜덤)
# 섞는다 !
# => 반환값 X (리턴값이 없다)

#############################################################

# 시간 조절
# from time import*
# sleep(시간 = 초)
#: 프로그램을 지연 (멈춘다.)

############################################################
'''
# 랜덤적으로 사각형을 그리는 프로그램 작성


from tkinter import*
from random import*
from time import*

win  = Tk()
can = Canvas(win,width=400,height=400) 
can.pack()

color = ['red','blue','yellow','pink','green','orange']

def draw_rect():
    x = randint(0,300)
    y = randint(0,300)
    w = randrange(100)
    h = randrange(100)

    can.create_rectangle(x,y,w,h,fill=choice(color))

for i in range(10):
    draw_rect() #함수 실행하고 ms단위로 들어감(0.01초)
    sleep(1)


win.mainloop()
'''
#######################################################

# 바인드 (이벤트)
# 버튼 누르거나 키를 누르거나 마우스를 눌렀을 때
# 실행을 도와주는 핸들러
# 사용 :
# 위젯.bind(event)

# 이벤트 발생시 Event Object 객체가 생성
# => 클래스 안에는 정보들을 가지고 있음.
# event 매개변수 꼭 작성되어야 함 ! 


'''
from tkinter import*
from random import*
from time import*

win  = Tk()

# 마우스를 클릭하면 그 위치를 출력해주는 이벤트프로그램

def onClick(event):
    print(event.x,"  ",event.y)


#           위젯,     함수 ()=X
win.bind("<Button-1>",onClick)




win.mainloop()
'''
# Draw Act

# "<Button-1>"  마우스 왼쪽버튼
# "<Button-2>"  마우스 휠
# "<Button-3>"  마우스 오른쪽버튼

# 드래그
# <B1 - Montion>    마우스 왼쪽버튼 누른 상태에서 움직일때
# <B2 - Montion>    마우스 휠을 누른 상태에서 움직일때
# <B3 - Montion>    마우스 오른쪽버튼 누른 상태에서 움직일때

# 더블클릭
#<Double-Button-1>   마우스 왼쪽 버튼 더블클릭
# B2 휠 B3 마우스오른쪽버튼


'''
from tkinter import*
from random import*
from time import*

win  = Tk()

# 마우스를 클릭하면 그 위치를 출력해주는 이벤트프로그램

def onClick(event):
    print(event.x,"  ",event.y)

def dleft(event):
    print("더블")

def mleft(event):
    print("모션")


#           위젯,     함수 ()=X
win.bind("<Button-1>",onClick)
win.bind("<Double-Button -1>",dleft)
win.bind("<B1-Motion>",mleft)




win.mainloop()
'''
# 키보드를 클릭했을때 <Key>
# char : 키보드를 누른 값을 문자로 변환
#   enter, f1, ctrl, 방향키 등이 문자로 표현X

# keycode : 아스키 코드값을 이용해서 반환
'''
focus_set() 포커스 위젯 설정 
<Key>
<Enter>
<Pause>
<Backspace>
<Caps_Lock>
<Escape>
<Home>
<End>
<Insert>
<Delete>
<Pgup>

방향키
<Up>
<Down>
<Right>
<Left>

'''




'''

# 모듈 추가하는 공간
from tkinter import*
from random import*
from time import*

# 함수
def onClick(event):
    print("키보드>",event.char)
    #print("키보드>",event.keycode)
    # 아스키코드값으로 출력됨 (모든키보드키)


# 클래스



#명령어 수행구간! main()

win  = Tk()
win.bind("<Key>",onClick)
win.focus_set() #키보드가 눌리면 포커스를 수정 

win.mainloop()
'''

# 애니메이션
# : 그림의 움직임을 주는 기법
# : 이벤트랑 같이 쓰임.

# move(객체,x,y)    : 이동 / 어떤 아이(객체)를 움직일건지,좌표
#   오른쪽이동 + / 왼쪽이동 -
#   아래 이동 + / 위로 이동 -
# update()  : 기존 그림을 지우고 새로 그릴 수 있도록 하는 메서드
# sleep()   : 시간 지연 함수
# after() : ms 단위로 설정되는 시간지연 /1초 = 1000



# 캔버스 공을 하나 만들도록 하자
'''
# 모듈 추가하는 공간
from tkinter import*
from random import*
from time import*

# 함수
def onClick(event):
    print("키보드>",event.keycode)


# 클래스


#애니메이션

win  = Tk()
can = Canvas(win,width=400,height=400)
can.pack()

id1=can.create_oval(10,10,50,50,fill='yellow')

for i in range(50):
    can.move(id1,5,0) # 오른쪽으로 5씩 이동
    can.after(100)    # 0.1 기다렸다가
    can.update()      # 새로 그림을 그리세요


win.mainloop()
'''
# 키보드를 누르는 방향에 따라 움직임이 달라지는 공 
'''

# 모듈 추가하는 공간
from tkinter import*
from random import*
from time import*

# 함수
def onClick(event):
    print("키보드>",event.keycode)

def move_left(event):
    can.move(id1,-5,0)
    can.after(10)
    can.update()

def move_right(event):
    can.move(id1,5,0)
    can.after(10)
    can.update()
    
# 클래스

#애니메이션

win  = Tk()
can = Canvas(win,width=400,height=400)
can.pack()

id1=can.create_oval(10,10,50,50,fill='yellow')

can.bind("<Left>",move_left)
can.bind("<Right>",move_right)
can.focus_set()


win.mainloop()
'''
# 클래스로 만든 키보드에 따라 공 이동시키기
'''

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
'''



















