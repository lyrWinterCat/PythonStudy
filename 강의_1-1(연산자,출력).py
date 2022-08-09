#한줄메모
"""여러줄 메모
 파이썬 + 1. 숫자 연산
          2. 문자열 연결

프로그래밍?
 - 인간의 언어를 컴퓨터가 인지할 수 있도록 형태를 변경시키는 작업

인터프리터
 - 프로그램을 한 단계씩 해석하여 실행
 - 1:1 대화형식

컴파일
 - 완성된 소스코드를 컴퓨터라 이해할 수 있는 기계 언어로 변환 (한번에)


확장자명 ->  .py

 연산자 +, - , *, 나눗셈(/) -> 나머지 %

 숫자 * 숫자 -> 연산 
 문자 * 숫자 -> 반복


나눗셈 / -> 결과 (몫) 실수
        // -> 결과 (몫) 정수
        % -> 나머지 값


비교연산자 : true, false (참 혹은 거짓)으로 결과값 도출 
    > 크니?
    >= 크거나 같니? 
     == 같니??
     != 다르니??    

"""
10 != 10 #달라야 참
10 == 20 #같아야 참

        #컴파일 (한번에 변경)

        # 출력 (결과값 확인)
        # 함수 : 입력, 출력
        
        # 내장함수 : 파이썬 기본 제공
        #   자주색
        
        # 사용자 정의 함수
        # : 프로그래머가 직접 만들어서 사용하는 함수
        
        # 정의 : 프로그래머가 만든 함수, 클래스를 미리 알려줄 때
        # 선언 : 메모리 할당
        # 파이썬 : 객체 지향 언어 
     

print(10!=10)
print(10)
print(1.25)
print("이예림")
print("A")


# print()
# 데이터를 화면에 출력한다.
# 개행(New Line) = 줄바꿈 기능이 포함되어 있음

# print(인수1, 인수2, ...)
# , 콤마 사용 : 데이터를 구별
# , 를 사용 했을시 띄어쓰기로 출력

# print("python") print() print()
# ; (세미콜론)
# -> 문장의 끝을 의미 


#원하는 식 가져오기 -> 아무곳이나 커서 대고 엔터


# sep : print함수 ,의 출력표시 지정

# end = print() print() 함수사이의 출력 서식을 지정할 때 사용
# 기본적인 줄바꿈 (\n)

# sep, end 순서는 상관 없다!
# 단!! 맨 뒤에 작성

# Q1. print()를 사용해서 좋아하는 과일 3가지를 출력

print("복숭아") ; print("수박") ; print("키위")
print("복숭아") , print("수박") , print("키위")

# Q2. prin()함수 한번만 써서 좋아하는 과일 3가지 출력
"""
[출력 형태]
딸기
애플망고
사과
"""
print("복숭아", "수박", "키위", end = "\n")


print("복숭아\n수박\n키위")
print("복숭아", "수박", "키위", sep = "\n")
