import time


class Person:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(self.name, "is not longer in use")


p1 = Person("John")
print(p1.name)
p1.name = "Mary"
print(p1.name)
print("How are you doing?")
