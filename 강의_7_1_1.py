# 1~5까지 출력 / for 를 이용해서!

'''
list1 = [1,2,3,4,5]

for a in list1:
    print(a)

'''

# 튜플을 사용해서 출력 
'''
tuple1 = ("이서희","이지희","이정희")

# 이서희님 입장하셨습니다 /출력
for name in tuple1:
    print(name,"님이 입장하셨습니다.")

'''
# hello world / 하나씩 출력
'''
for str1 in "hello world":
    print(str1)

'''
# 딕셔너리?
# 딕셔너리 자체를 반복 : key값만 반복!
# value 값은 어떻게 가져올까..?

'''
dict1 = {1:"python",2:"java",3:"Zython"}
for key in dict1:
    print(key)
'''
# .values() 사용!
'''
dict1 = {1:"python",2:"java",3:"Zython"}
for value in dict1.values():
    print(value)

'''
# key,value 를 동시에 뽑아서, 동시에 출력?
# items()
# key , value 동시에 뽑아오는 내장함수

'''
dict1 = {1:"python",2:"java",3:"Zython"}
#[(1,"python"),(2,"java"),(3,"Zython")]
for key, value in dict1.items():
    print(key, " ",value)
'''
#range
# 1부터 100까지 짝수 홀수합
# 각각 저장해서 반복이 끝나면
# 출력하는 프로그램

'''
odd = 0  #홀수
even = 0 #짝수

for number in range(1,101):
    if number % 2==0:
        even += number
    else:
        odd += number

print("반복문끝")
print("홀수:",odd,"짝수:",even)
        
'''
# 구구단 출력~ 3단! range 이용!
#range()
# 출력  : 3*1=3
'''
내 식

count = 0
for number in range(1,10):
    count += 3
    print("3 * ",number,"=",count)

샘샘님 식
for i in range(1,10):
    print("3 *",i,"=",(3*i))

만약 while 식이라면?

i = 1
while i i <=9:
    print("3 *",i,"=",(3*i))
    i+=1


'''
# 예문) 시험을 치른 후 맞은 개수를 알려주는 프로그램
'''
내 식

str1 = str(input("이름 : "))
int1 = int(input("문제 개수 : "))
print("***************************")

quest = 0
for i in range(1,(int1)+1):
    print(i,"번 문제를 해결했나요?(y/n)")
    if str(input()) == "y":
        quest +=1
print("***************************")
print(str1+" 학생, 총 ",str(quest)+"문제를 해결했습니다.")

'''
# 예문 센세 답
'''
name = input("이름>")
num = int(input("문제 개수>"))

score = 0  #총 문제 맞춘 개수 저장변수
print("*"*10)
for i in range(1,num+1):
    print(i,"번 문제를 해결했나요?(y/n):")

    ans = input()

    if ans == 'y':
        score += 1
print("*"*10)
print( name,"학생, 총", score,"문제를 해결했습니다.")






