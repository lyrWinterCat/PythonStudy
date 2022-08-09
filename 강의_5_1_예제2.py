#1 편의점에서 재고 관리를 수행하는 프로그램 작성
# 판매하는 물건에 재고를 딕셔너리로 저장

# 커피음료 : 7
# 펜 : 3
# 종이컵 : 2
# 우유 : 1
# 콜라 : 4

# 커피에 재고 얼마 있어요?
# 재고 개수 : **   -> 출력값

# 재고 중에 사이다가 있니? 정답 출력!

shop = {"커피" : 7, "펜" : 3, "종이컵" : 2, "우유" : 1,"콜라" : 4}
quest = input("원하시는 상품을 입력하세요>")
answer = shop[quest]
print("재고 개수 : ",answer)

print("사이다" in shop)

#2 영한 사전 만들기
# 영어를 입력 하면 그에 대한 한글로 답이 출력되면 됨!

# cat -> 고양이 출력
# 딕셔너리명 : animallist

# cat
# rabbit
# puppy

# sparrow가 영한사전에 있니? 결과 출력! 

animallist = {"cat":"고양이","rabbit":"토끼","puppy":"강아지"}
quest1 = input("영단어를 입력하세요>")
answer1 = animallist[quest1]
print(answer1)
print("sparrow" in animallist)


