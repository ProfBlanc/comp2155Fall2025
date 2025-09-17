"""
Cat Class
Lion Class
Tiger Class
Liger Class
    part Lion, part Tiger
"""
import random


class Cat:
    def __init__(self, name, paws):
        self.name = name
        self.paws = paws

    @property
    def paws(self): return self.__paws
    @paws.setter
    def paws(self, value):
        if not isinstance(value, int) or not value == 4 : raise ValueError("Invalid paws")
        self.__paws = value
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3: raise ValueError("Invalid name")
        self.__name = value

    def eat(self, food): return f"{self.name} is eating {food}"
    def sleep(self, duration): return f"{self.name} is sleeping for {duration} hours"


class Lion(Cat):
    def __init__(self, name, paws, mane):
        super().__init__(name, paws)
        self.mane = mane
    @property
    def mane(self): return self.__mane
    @mane.setter
    def mane(self, value):
        if not isinstance(value, str): raise TypeError("Invalid mane data type")
        self.__mane = value
    def roar(self): return f"{self.name} is roaring"

class Tiger(Cat):
    def __init__(self, name, paws, stripes):
        Cat.__init__(self, name, paws)
        self.stripes = stripes
    @property
    def stripes(self): return self.__stripes
    @stripes.setter
    def stripes(self, value):
        if not isinstance(value, int) or value < 10: raise ValueError("Invalid stripes values")
        self.__stripes = value
    def show_teeth(self):
        number_of_teeth = random.randint(10, 50)
        return f"{self.name} is showing {number_of_teeth} teeth"

class Liger(Lion, Tiger):
    def __init__(self, name, paws, mane, stripes, size="big"):
        Tiger.__init__(self=self, name=name, paws=paws, stripes=stripes)
        self.mane = mane
        self.size = size
    def relax(self): return f"{self.name} is relaxing"


cat = Cat("Cat", 4)
lion = Lion("Lion", 4, "medium-sized mane")
tiger = Tiger("Tiger", 4, 15)
liger = Liger(name="Liger", paws=4, mane="large-sized mane",
              stripes=20, size="very big")

print(liger.eat("food"), liger.show_teeth(), liger.sleep(3), liger.relax(), liger.roar())