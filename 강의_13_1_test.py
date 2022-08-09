
# C드라이브 안에 Person_test.txt

with open("C:\\AAA\\이예림1.txt",'a') as out:
    name = input("이름:")
    age = int(input("나이:"))

    out.write("이름>%s"%name\n)
    out.write("나이>%d"%age)

  
#out.write("이름:> 이예림\n")
#out.write("나이:> 27 \n")

