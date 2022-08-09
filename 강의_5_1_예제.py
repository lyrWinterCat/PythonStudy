# input()을 이용해서 ID와 PW 저장

'''

id1 = input("ID를 입력하세요>")
pw = input("PW를 입력하세요>")
idlist1 = {id1 : pw}
print("id1>",idlist1)
print("pw>",idlist1[id1])

'''

#  print id1 에서 idlist1 -> id1 라고 쓰면
# 그냥 나오기는 함... 어떻게 해야 dict 안에 있는 id1를 표기해서 가져올 수 있을까

# dict 안에서 key 나 value 값 가져오는 법은??
id1 = input("ID를 입력하세요>")
pw = input("pw를 입력하세요>")
idlist1 = {id1:pw}
print("id>", idlist1.keys());print("pw>",idlist1.values())

#??

'''
id> dict_keys(['love'])
pw> dict_values(['live'])
'''

