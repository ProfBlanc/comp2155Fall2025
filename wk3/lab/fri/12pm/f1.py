"""
Cat
    name
    paws
Lion: Cat
    mane
Tiger: Cat
    stripes
Liger: Lion, Tiger
    size
"""

class Cat:
    def __init__(self, name, paws):
        self.name = name
        self.paws = paws
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) < 3:
            raise ValueError("Invalid name")
        self.__name = value
    @property
    def paws(self): return self.__paws
    @paws.setter
    def paws(self, value):
        if not isinstance(value, int) and not value == 4:
            raise ValueError("Invalid paws")
        self.__paws = value
    def __str__(self): return f"{self.name} has {self.paws} paws ...."

class Lion(Cat):
    def __init__(self, name, paws, mane):
        super().__init__(name=name, paws=paws)
        self.mane = mane
    @property
    def mane(self): return self.__mane
    @mane.setter
    def mane(self, value):
        if not isinstance(value, str): raise TypeError("Invalid mane")
        self.__mane = value

class Tiger(Cat):
    def __init__(self, name, paws, stripes):
        super().__init__(name=name, paws=paws)
        self.stripes = stripes
    @property
    def stripes(self): return self.__stripes
    @stripes.setter
    def stripes(self, value):
        if not isinstance(value, int): raise TypeError("Invalid stripes")
        self.__stripes = value

class Liger(Lion, Tiger):
    def __init__(self, name, paws, mane, stripes, size):
        Tiger.__init__(self=self, name=name, paws=paws, stripes=stripes)
        self.mane = mane
        self.size = size
    @property
    def size(self): return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, str): raise TypeError("Size is invalid")
        self.__size = value

cat = Cat("Cat", 4)
lion = Lion("Lion", 4, "cool mane")
tiger = Tiger("Tiger", 4, 20)
liger = Liger("Liger", 4, "big mane", 30, "very big")
print(cat)
print(lion)
print(tiger)
print(liger)
