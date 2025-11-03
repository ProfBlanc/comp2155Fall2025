class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):  # destructor: invoked once object is no longer used
        print(f"Person {self.name} no longer referenced")

p1 = Person("Test")
p2 = Person("Case")

