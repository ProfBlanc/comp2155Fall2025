"""
Cat
    name
    paws
Lion: Cat
    mane
    roars
Tiger: Cat
    stripes

Liger: Lion & Tiger
    size

"""
import random


class Cat:
    def __init__(self, name, paws):
        self.name = name
        self.paws = paws
    def __str__(self): return f"{self.name} has {self.paws} paws"
class Lion(Cat):
    def __init__(self, name, paws, mane, roar):
        super().__init__(name, paws)
        self.mane = mane
        self.roar = roar
    def __str__(self): return super().__str__() \
        + f" and has a {self.mane} mane and has a {self.roar} roar"

    def __add__(self, other):
        if isinstance(other, Lion):
            return Lion(
                name=f"{self.name}-{other.name}",
                paws=round((self.paws + other.paws) / 2, 0),
                roar=f"{self.roar}-{other.roar}",
                mane=f"{self.mane}-{other.mane}"
            )

        elif isinstance(other, Tiger):
            return Liger(
                name=f"{self.name}-{other.name}",
                paws=round((self.paws + other.paws) / 2, 0),
                roar=f"{self.roar}",
                mane=f"{self.mane}",
                stripes=other.stripes,
                life_span=random.randint(1,5)
            )


class Tiger(Cat):
    def __init__(self, name, paws, stripes):
        super().__init__(name, paws)
        self.stripes = stripes

    def __str__(self): return super().__str__ () \
       + f" and has {self.stripes} stripes"

    def __add__(self, other):
        if isinstance(other, Tiger):
            return Tiger(
                name=f"{self.name}-{other.name}",
                paws=round((self.paws + other.paws) / 2, 0),
                stripes=round((self.stripes + other.stripes) / 2, 0)
            )

        elif isinstance(other, Lion):
            return Liger(
                name=f"{self.name}-{other.name}",
                paws=round((self.paws + other.paws) / 2, 0),
                roar="little",
                mane=f"small",
                stripes=self.stripes,
                life_span=random.randint(1,5)
            )


class Liger(Tiger, Lion):
    def __init__(self, name, paws, mane, roar, stripes, life_span):
        Lion.__init__(self, name, paws, mane, roar)
        self.stripes = stripes
        self.life_span = life_span
    def __str__(self):
        return Lion.__str__(self) \
            + Tiger.__str__(self).replace(Lion.__str__(self), "") \
            + f" and has a life span of {self.life_span}"


cat = Cat("Cat", 4)
tiger = Tiger(name="Tiger", paws=5, stripes=20)
lion = Lion(name="Lion", paws=6, roar="loud", mane="big")
liger = Liger(name="Liger", paws=7, roar="thundering",
              mane="fro", life_span=5, stripes=15)

print(cat, tiger, lion,liger, sep='\n')

liger2 = lion + tiger
liger3 = tiger + lion

print(liger2, liger3, sep="\n")