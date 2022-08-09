'''
"r" : 읽기모드 (read mode) = 파일의 처음부터 읽는다
"w" : 쓰기모드 (write mode) = 파일의 처음부터 쓴다.
파일이 없으면 생성된다. 만약 파일이 존재하면 기존 내용은 지워짐
"a" : 추가모드 (append mode) = 파일의 끝에 쓴다.
파일이 없으면 생성된다.

"r+" : 읽기와 쓰기모드 = 파일에 읽고 쓸 수 있는 모드. 모드를
변경하려면 seek() 가 호출되어야 함
'''

# 파일 입출력
'''
파일의 객체를 생성

객체 = open("파일경로", 모드)

객체.close()

=> 13_1_test 참고 

f = open("TestFile.txt",'w')
    # 파일이 생성되는 경로를 따로 지정하지 않으면
    # 파이썬 스크립트가 위치한 동일한 경로에 파일을 생성!

    # 기본적인 위치 : 내가 지정한 경로 

f.close()
    # 파일 객체를 생성했으면 반드시 닫아주어야 함!! 
'''


'''
f = open("TestFile.txt",'w')
    # 파일 입력할 때는 write() : 파일에 데이터를 입력하는 함수
    # 복수의 데이터를 입력할 수 없다
    # 문자열 데이터만 입력 가능함
    # 기본 자료형들을 저장하고 싶을 경우 pickle 모듈 사용해야함
    # 개행(줄바꿈 포함 x) => 신경을 써야 함

f.write("이서희\n") --> 끝에 문자 : 줄바꿈 !
f.write("파이썬 15일째")
f.write(1) --> X

f.close()

# 시퀀스 문자
# 특수문자 \n 줄바꿈
'''

# 문자열 포멧팅

# %d : 정수
# %s : 문자열 
# %f : 실수
#    : .6자리까지 표현
# %.자리수f: 원하는 자리수까지 보고싶다

# %c : 하나의 문자를 표현


# 문자열 안에 정수를 삽입
# "문자열 안에 포멧 작성"%변수,데이터


'''
f = open("MyTestFile.txt",'w')

for i in range(1,11):
    data = "%d번째 줄 입니다.\n"% i
    f.write(data)


f.close()
'''






# 파일을 여러개 생성

namelist = ["이서희","이지희","설난이","클리니"]

# 파일명작성 = "문자열"


for i in namelist:
    f = open("[%s].txt"% i,"w")
    name = input("이름>")
    age = int(input("나이>"))
    g = input("성별>")
    phone = input("폰>")
    

    
    f.write('''이름 : %s
나이: %d
성별: %s
폰번호: %s
'''%(name,age,g,phone))

# 포멧팅을 두개 이상 할 경우에는 콤마 구별!
# %(데이터1, 데이터2, ....)
f.close()


'''
# 읽기모드
# Readline(): 파일의 문장 한 라인을 읽어드림

# Readlines(): 파일의 모든 라인을 읽어서 각각의
#           요소를 갖는 리스트로 반환 


# Read(): 파일의 내용 전체를 문자열로 리턴
# Read(숫자): 데이터를 (숫자)개 읽어와라! 




# 출력 : 저장 텍스트파일로...
#       : 파이썬 프로그램에서 데이터를 내보낸다.

f = open("MyTestFile.txt",'w')

for i in range(1,101):
    data = "%d번째 줄 입니다.\n"% i
    f.write(data)

f.close()



# 입력 : 파이썬 프로그램으로 데이터를 읽어들인다.
# 읽기모드일 경우 모드를 생략해도 상관 없다!


input1 = open("MyTestFile.txt")



#print(input1.read(20))


print(input1.readlines())  

# ?? 몇줄 있는지 모를경우 
#for i in input1.readlines():
#    print(i,end="")


f.close()



# 스트림 : 데이터의 연속적인 흐름
#        : 데이터들의 다리
#        : 단방향 통신(입력, 출력)

'''

# pickle 모듈
# : 텍스트 파일로 저장할때
# : 자료형들을 파일로 저장(기본자료형, 클래스)
# : pickle로 데이터를 저장하고 불러올 때
#   파일 바이트 형식으로 읽거나 써진다.

# 파일명 .bin



# pickle 모듈
# : 텍스트 파일로 저장할때
# : 자료형들을 파일로 저장(기본자료형, 클래스)
# : pickle로 데이터를 저장하고 불러올 때
#   파일 바이트 형식으로 읽거나 써진다.

# 파일명 .bin

# 'wb', 'rb'



# dump(데이터,파일): 저장
# load(파일)      : 읽기


#import pickle

from pickle import *

f = open("byte_file.bin",'wb')

#pickle.
dump('hello world',f)
#pickle.
dump(12345,f)
#pickle.
dump(3.14,f)
#pickle.
dump([1,2,3,4],f)
#pickle.
dump({1:"python",2:"Java"},f)

f.close()


f = open("byte_file.bin",'rb')
# 덤프가 저장한 순서대로 로드된다. 

d = load(f)
print(d,type(d))

d = load(f)
print(d,type(d))

d = load(f)
print(d,type(d))

d = load(f)
print(d,type(d))

d = load(f)
print(d,type(d))

f.close() 

# with
# : 자동적으로 파일을 닫는 역할
# : 파일의 객체를 닫지 않으면 에러 !
# : 저장 X

with open("파일명 경로", '모드') as 객체:
    pass # write()
         # pickle 모듈로 저장 

#  어제 저장한 AAA 폴더 안에 본인 이름의 텍스트 파일 저장
# 파일 안에 본인 정보 (이름, 나이)
# 입출력 해보세요 

with open("C:\\AAA\\이예림1.txt",'a') as out:
    name = input("이름:")
    age = int(input("나이:"))

out.write("이름:> 이예림\n")
out.write("나이:> 27 \n")

#입력받아서 저장
out.write("이름>%s"%name\n)
out.write("나이>%d"%age)

