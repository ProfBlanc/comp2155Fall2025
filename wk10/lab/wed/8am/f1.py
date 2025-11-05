class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} has been destroyed. No more running referencces")



p1 = Person("Ben")
p2 = Person("John")