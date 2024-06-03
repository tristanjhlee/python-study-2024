#클래스 변수 사용법
class Person:
    li = []
    def __init__(self, sp):
        Person.li.append(sp)

    def disp(self):
        print(Person.li)

p1 = Person('우유')
p1.disp()
p2 = Person('콜라')
p2.disp()
p3 = Person('주스')
p3.disp()
'''
# 인스턴트 변수 사용법
class Person:
    def __init__(self, sp):
        self.li = []
        self.li.append(sp)

    def disp(self):
        print(self.li)

p1 = Person('우유')
p1.disp()
p2 = Person('콜라')
p2.disp()
p3 = Person('주스')
p3.disp()
'''