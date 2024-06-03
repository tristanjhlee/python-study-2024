#전화번호부 만들기

class Person:
    def __init__(self):
        self.name = input('이름: ')
        self.age = int(input('나이: '))

    def disp(self):
        print(self.name + ': ' + str(self.age))

li = []

for i in range (3):
    li.append(Person())
for i in li:
    i.disp()