class Person:
    name = ""
    age = 0
    job = ""
    hei = 0.0
    wei = 0
    address = ""
    phone = ""

    def init(self,name,age,job,hei,wei,address,phone):
        self.name = name
        self.age = age
        self.job = job
        self.hei = hei
        self.wei = wei
        self.address = address
        self.phone = phone
        print("객체 생성 완료!") 

서희 = Person()
서희.init("이서희",20,"강사",160.15,40
        ,"서울시 강남구","010-1234-1234")

다다 = Person()
다다.init("다다",10,"초등생",120.58,30,"경기도 오산시",
        "010-2345-2345")

# 변수들을 관리하고 유지하기 위해서 기능들이 추가가 됨!
# 멤버필드들을 변경,수정하고 삭제하고 관리하기 위해서
# 만들어진 것 : 기능 
