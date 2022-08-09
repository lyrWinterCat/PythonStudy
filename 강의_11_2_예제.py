# 사용자 예외 만들기
# 프로그래머가 직접 예외를 만든다
#  Exception  클래스 (예외에 대한 클래스들의 부모)
# 상속!!

'''
class MyError(Exception):
    def __init__(self,value):
        self.value = value


#내가 직접 만든 예외를 문자열로 출력
# 연산자 오버로딩
    def __str__(self):
        return self.value

try:
    raise MyError('직접만든 오류!')

except Exception as e:
    print(e)
    print(type(e))


***********************************
try:
    raise Exception('인덱스')
except Exception as e:
    print(e)
    print(type(e))

    
인덱스
<class 'Exception'>
'''





