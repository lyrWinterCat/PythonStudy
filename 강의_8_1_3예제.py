# 호출 순서 (필기 참고) 
def a():
    c = b()
    return c

def b():
    e = d()
    return e

def d():
    return "다다"


#main

a()
