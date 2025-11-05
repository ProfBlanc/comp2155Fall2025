class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("The object", self.name, "no longer exists")

p1 = Person("John")
p2 = Person("Mary")

p1.name = "Boo"

p1.name = "Foo"
