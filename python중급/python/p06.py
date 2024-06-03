class sj:
    def __init__(self):
        self.kor = 90
        self.__eng = 77
        self. math= 88

    def geteng (self):
        return self.__eng

    def seteng (self, eng):
        self.__eng = eng

s1 = sj()
s1.seteng(100)
print(s1.geteng())