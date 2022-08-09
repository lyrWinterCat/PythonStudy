# 데이터베이스 사용할 때

# 데이터 변경 
'''
수정할 데이터가 어디에 있는지w어떤 데이터로 할건지     

update 테이블명 set 필드명 where 수정 

'''

from sqlite3 import *

con = connect("Book_list.db")
cur = con.cursor()

#테이블 생성 
#cur.execute('create table Booklist1(Name text,Page text);')

# 생성된 테이블에다 데이터를 추가
cur.execute('insert into Booklist1 values("한국사","300")')
cur.execute('insert into Booklist1 values("중국사","200")')

name = input("책이름>>")
page = input("페이지>>") 
cur.execute('insert into Booklist1 values(?,?)',(name,page))

con.commit()
con.close()






# 데이터 삭제

from sqlite3 import *

con = connect("Book_list.db")
cur = con.cursor()

sql = "delete from Booklist1 where Name=?"
data = ("한국사",)

cur.execute(sql,data)

con.commit()
con.close()

#최종버전 
from sqlite3 import *

con = connect("phone_list.db")
cur = con.cursor()

#생성
#cur.execute('create table Booklist1(Name text,Page text);')

#데이터삽입
#cur.execute('insert into Booklist1 values("한국사","300")')
#cur.execute('insert into Booklist1 values("중국사","200")')

#값 수정
#cur.execute('update Booklist1 Set Name=? where Name=?'
#            ,('한국사','중국사'))

#값 삭제
cur.execute('delete from Booklist1 where Name=?',('한국사',))
#튜플로 인식하기위해 하나의 데이터 뒤에 ',' 찍어주어야함 

con.commit()
con.close()


##################################################

# tkinter 모듈 
'''
: GUI 그래픽을 지원 

: 파이썬에서 그래픽 사용자 인터페이스
(Graphical User Interface)를 개발할 때 필요한 모듈

tkinter은 예전부터 유닉스 계열에서 사용되던
Tcl/Tk 위에 객체 지향 계층을 입힌 것.
Tk는 John Osterhout에 의하여 Tcl 스크립팅 언어를
위한 GUL 확장으로 개발!

단순 위젯 :
Button, Canavs, Checkbutton,Entry,Label,Message 등

컨테이너 컴포넌트 :
다른 컴포넌트를 안에 포함할 수 있는 컴포넌트
Frame, Toplevel, LavelFrame, PanedWindow 등

:: 우리는 이걸로 비행기게임을 만들거야~
'''
# 위젯들은 모두 클래스
# : 원하는 객체를 생성해서 사용
'''
* 라벨 형태 설정
이름/의미/기본값/속성

width/라벨의 너비/0/상수
height/라벨의 높이/0/상수
relief/라벨의 테두리모양/flat/flat,groove,raised,ridge,solid,sunken
borderwidth=bd/라벨의 테두리두께/2/상수
background=bg/라벨의 배경색상/systemButtonFace/color(문자열)
foreground=fg/라벨의문자열색상/systemButtonFace/color
padx/라벨의테두리와내용의가로여백/1/상수
pady/라벨의테두리와내용의세로여백/1/상수 



'''


# tkinter 모듈

from tkinter import *

win = Tk() # 윈도우창을 생성
win.title("제목없는 윈도우") # 윈도우 제목

# 크기 및 위치 geometry("너비x높이+x좌표+y좌표")
win.geometry("300x300+100+100")

# 라벨 생성 
label = Label(win,text="파이썬16",bg='red',fg='white')
# 라벨 화면 배치 관리자
label.pack()


#버튼생성
btn1 = Button(win,text='첫번째버튼')
btn2 = Button(win,text='두번째버튼')

#위치 직접지정 
btn1.place(x=0,y=0)
btn2.place(x=100,y=100)
#place(x,y) : 윈도우창 안에서 x,y 좌표 위치를 잡아서
#           위젯들을 표시해 준다.
#grid(행,열/가로:row,세로:colum) : 격자배치


# pack() : 윈도우 자체 크기로 압축해서 자동지정
#       : 특별한 지정이 없으면 무조건 top (위쪽에 선언)
#       side() : 위치 지정 가능 ! 기본적으로 위에서 아래로 추가
#           (LEFT,RIGHT,TOP...)

#btn1.pack(side = LEFT)
#btn2.pack(side = LEFT)

# ID/PW 창 만들기 
# Entry : 텍스트 필드
#   :사용자로부터 입력을 받을 때 사용하는 텍스트창
#   :입력한 문자열을 가지고 올 수도 있다 !
#   = 이벤트 필요

Label(win,text="ID:").grid(row=0)
Label(win,text="PW:").grid(row=1)

e1 = Entry(win)
e2 = Entry(win)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


# 이벤트: 특정 상황이 발생했을때 내가 실행하겠다!
# = bind
# : 위젯들에서 특정한 상황이 발생했을 때 수행할 수 있는 함수들로
# 연결하는 기능

#ex) 버튼을 누르면 안녕하세요 출력

def process():
    print("안녕하세요?")

btn1 = Button(win,text="클릭하세요",command=process)
btn1.pack()

def my_call():
    #버튼이누르면 클릭하세요->버튼이 눌렸어요 로 변경
    # btn1['text']='버튼이 눌렸습니다.'

    #다시누르면 원래대로 돌아가도록 수정
    #print(btn1['text'])
    if btn1['text'] =='클릭하세요!':
        btn1['text'] = '버튼이 눌렸습니다.'
    else:
        btn1['text'] = '클릭하세요!'


btn1 = Button(win,text="클릭하세요!",command=my_call)
btn1.pack()


win.mainloop() # 윈도우창이 종료 될때까지
            #윈도우를 실행시키겠다. 

###############################################################

from tkinter import *

k = Tk() # 윈도우창을 생성
k.title("제목없는 윈도우") # 윈도우 제목

# 크기 및 위치 geometry("너비x높이+x좌표+y좌표")
#k.geometry("300x300+100+100")

# 캔버스 Canvas 위젯 : 스케치북!
#   : 윈도우 판 위에다가 붙일거야!
#   선, 다각형, 원... 가능
#   너비와 높이 설정
# Canvas(윈도우창,파라미터1,파라미터2...(매개변수))

can = Canvas(k,width=400,height=300,bg='white')
can.pack()


k.mainloop() 

















