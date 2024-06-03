class Person:
    def __init__(self):
        self.name = 'eric'
        self.age = 25

    def say (self):
        pass
class Korean (Person):
    def __init__(self):
        super().__init__()
        self.lang = 'Korean'

    def say(self):
        print('안녕')

class American (Person):
    def __init__(self):
        super().__init__()
        self.lang = 'English'

    def say(self):
        print('Hello')

k1 = Korean()
print (k1.name, k1.age, k1.lang)
k1.say()

a1 = American()
print (a1.name, a1.age, a1.lang)
a1.say()