# 반복문 중간에 중지하면 생기는 Error
# StopIteration

# 1반 키를 저장하는 딕셔너리
# 2반 키를 저장하는 딕셔너리

school = {'1반':[150,160,170,180,190]
          ,'2반':[190,150,179,160,199]}

# 190이 넘는 학생을 발견하면 반복을 종료
# 예외를 발생시키기!

#1,2 반 190 넘는 학생이 있습니다.

#내식 ㅠㅠ
for num,stu in school.items():
    print(num,stu)
    try:
        for h in stu:
            print("현재 측정하는 학생키는",h)
            if h >=190:
                raise Exception

    except Exception:
        print(num,"190 넘는 학생이 있습니다.")
        

#답

try:
    for number,stu in school.items():
        for s in stu:
            if s > 190:
                print(number,'190넘는 학생이 있습니다.')
                raise StopIteration

except StopIteration:
    print('정상종료')
    





















