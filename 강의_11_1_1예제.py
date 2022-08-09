# 클래스명
# 예외처리구문자체 = 클래스
# 다중 예외처리 가능



# 두 개의 정수를 받아서 나누는 문장
'''
try:
    a = int(input("첫번째 정수>"))
    b = int(input("두번째 정수>"))
    print("a/b=",a/b)
    
except ValueError:
    print("값이 적절하지 않습니다.")

except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")

print("예외처리구문")
'''

'''
try:
    a = int(input("첫번째 정수>"))
    b = int(input("두번째 정수>"))
    print("a/b=",a/b)
    a = [1,2]
    print(a[3])


# Exception = 여러 에러들의 부모클래스
except Exception as e:
    print(e)
    #pass #특정 에러 발생할 경우 통과
          # 오류 회피하기
finally:
    print("무조건 실행구문")



print("예외처리구문")
'''

def rsp(a,b):
    str1 = ['가위','바위','보']

    if a not in str1:
        raise ValueError
    
    if b not in str1:
        raise ZeroDivisionError

try:
    rsp('가위','바')
except Exception:
    a=2
    
except ValueError:
    print("값이 잘못 되었습니다.")
    a=1


except ZeroDivisionError: 
    #print("아이고 제대로 했다")
    a=0

print(a)


















