# 이미지 표현하기
# GUI 에서 버튼, 라벨
# 라벨 (표시) 위젯


# 그림을 올릴때 중요한 것  : 위치 !!

# + 실행 모듈과 그림이 같은 폴더에 있으면
# 경로를 따로 줄 필요는 X
# "파일명.확장자" 문자열로 주면 됨 


# PhotoImage(file="파일명.확장자명")

"""
from tkinter import*

win = Tk()
photo = PhotoImage(file='18_elephant.png')
w=Label(win,image=photo)
#w.photo = photo
w.pack()

win.mainloop()
"""
#절대경로 / 사용경로
# 절대경로 : C드라이브에서 밑으로 쭈우욱 내려오는것
# photo = PhotoImage(file='C:\\18_elephant.png')


# 스레드
# 프로그램 : 실행 가능한 파일
# 프로세스 : 실행 중인 프로그램(메모리)
# 스레드 : 프로세스 안에서 실제 작업을
#       수행하는 것! (가장 작은 단위)
#       실제 작업을 하는 가장 작은 단위 ! 

# ex) 워드프로그램, 한글 프로그램이 있을 때 
# : 프로그램 안에서 맞춤법 검사하고 변경하는 애들 = 스레드

# Threading 모듈 안에 Thread 클래스 










