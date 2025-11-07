class Person:
    def __init__(self, name):
        self.name = name
    def __del__(self):  # once there are no more references to the object
        print(self.name + " is not longer is use")

p1 = Person("John")
p2 = Person("Mary")