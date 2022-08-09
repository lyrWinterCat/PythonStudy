'''
내가 하고자 한 식 
class Cellphone:
    def __init__(self,model,number,chord):
        self.model = model
        self.number = number
        self.chord = chord
    def setNumber(self,str1):
        self.number=st1
    def getModel():
        return self.model
    def getChord():
        return self.chord
    def getNumber():
        return self.number

class D_caPhone(Cellphone):
    def pixel(self):


class MP3Phone(Cellphone):
    def size(self):
'''

# 답 
class CellPhone:
    def __init__(self,model="무명폰",number="",chord=5):
        self.model = model
        self.number = number
        self.chord = chord

    def setNumber(self,str1):
        self.number = st1
        print("폰번호 수정됨")
    def getModel(self):
        return self.model
    def getChord(self):
        return self.chord
    def getNumber(self):
        return self.number

class D_caPhone(CellPhone):
    def __init__(self,pixel,number,chord,model):
        super(). __init__(model,number,chord)
        self.pixel = pixel
        print("디카폰!")

class MP3Phone(CellPhone):
    def __init__(self,size,number,chord,model):
        super(). __init__(model,number,chord)
        self.size = size
        print("엠피폰!")

    #오버라이딩
    def getNumber(self):
        print("MP3폰 안녕~",self.number)


a1 = MP3Phone(10,"010-123",5,"Mp3삼성폰")
b1 = D_caPhone(500,"010-222",0,"디카LG폰")
