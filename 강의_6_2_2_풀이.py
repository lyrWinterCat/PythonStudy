'''
count = 1
while count != 10:
        print("3","*",count,"=",3*count)
        count += 1
        
'''


# * 예제
'''
count = 1
while count <=5:
    print("*"*count)
    count +=1
'''

# 1 예제
'''
count = 1
while count <=5:
    if count <4:
        print(" "*(4-count)+"1"*(2*count-1))
    if count >=4:
        print(" "*(count-2)+"1"*(11-(2*count)))
    count +=1
''' 


# str1 = "123456"
# str2 = "ABCDEF"
'''
count = 1

while count <=3:
    if count <=1:
        print(str1[0:count+2]+str2[ :count])
    if count >=2:
        print(str1[(2*count-1):2*count]+str2[

'''

'''
str1 = "123456"
str2 = "ABCDEF"

str1Num=0
str2Num=0
count=1
while count <=3:
    print(str1[str1Num:str1Num+4-count]+str2[str2Num:str2Num+count])
    str1Num = str1Num + 4-count
    str2Num = str2Num + count
    count+=1
'''


# *   *
# ** ** 문제

'''

count = 1
while count <=5:
    print("*"*count+" "*(10-2*count)+"*"*count)
    count +=1

'''
