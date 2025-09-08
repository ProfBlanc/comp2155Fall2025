"""
TShirt class
    -attributes
    -methods
        -magic methods: e.g.: tostring and add
        -special methods: static & class
    encapsulation: hiding data
        getters and setters



"""

class TShirt:
    def __init__(self, size="L", color="grey"):
        self.size = size
        self.color = color

    # getter and setter aka accessors and mutators

    # decorator: disguising method as __________
    @property
    def size(self): return self.__size

    def size_fullname(self):
        if self.size == "S":
            return "Small"
        elif self.size == "M":
            return "Medium"
        else:
            return "Unknown"



    @size.setter
    def size(self, value):
        if not isinstance(value, str):
            raise ValueError("Size must be string")
        elif len(value) < 1 or len(value) > 3:
            raise ValueError("Invalid size entry. Size has too many characters")
        elif value.upper() not in TShirt.available_sizes():
            raise ValueError(f"{value} is not a valid size")
        self.__size = value.upper()
    @staticmethod
    def available_sizes():
        return "S,M,L,XL,XXL".split(",")

    def __str__(self):
            # return f"TShirt has a size of {self.size} and a color of {self.color}"
            return f"{self.color} {self.size} TShirt"

    @classmethod
    def undershirt(cls):
        return cls(color="white", size="M")

    def __add__(self, other):
        if not isinstance(other, TShirt):
            raise ValueError("unsupported operands between TShirt and " + type(other))



        return TShirt(color=f"{self.color}-{other.color}", size=(self.size + other.size)[:3])


uts = TShirt.undershirt()
print(uts)

shirt1 = TShirt("m", "grey")
print(shirt1.size, shirt1.color)
print(shirt1)
print(shirt1.size_fullname())
print(TShirt.available_sizes())


#shirt2 = TShirt()

