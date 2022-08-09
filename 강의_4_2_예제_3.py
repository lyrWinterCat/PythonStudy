#연필과 펜의 구입하는 개수에 따라 총 가격을 출력하는 프로그램

#연펠은 1000원, 펜은 2000원
#변수 num_pencil, num_pen
# 이용해서 입력함수를 이용해서 각각 입력받고
# 변수 total_price에 저장한다

num_pencil = int(input("연필의 갯수를 입력하세요>"))
num_pen = int(input("펜의 갯수를 입력하세요>"))

total_price = 1000*num_pencil + 2000*num_pen
print("연필과 펜의 총 가격은 ",total_price,"입니다.")

'''
모범답안
num_pencil = int(input("연필은 몇개 구입하시겠습니까?>"))
num_pen = int(input("펜은 몇개 구입하시겠습니까?>"))

total_price = (1000*num_pencil) + (2000*num_pen)

print("연필과 펜의 총 가격은 ",total_price,"입니다.")
'''











