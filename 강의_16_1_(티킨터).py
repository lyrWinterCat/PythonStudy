# tkinter 모듈

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


k.mainloop() # 윈도우창이 종료 될때까지
            #윈도우를 실행시키겠다. 
