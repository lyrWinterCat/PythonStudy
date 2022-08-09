#국어, 수학, 영어 점수를 각각의 변수에 저장한 후에
# 총점과 평균을 내는 프로그램을 만들어 보시오

kor = int(input("국어점수>"))
eng = int(input("영어점수>"))
math = int(input("수학점수>"))


total = kor + eng + math
avg = total / 3

print("총점>",total)
print("평균>",avg)


# 나눌때 // 한다면 정수로 나옴!
