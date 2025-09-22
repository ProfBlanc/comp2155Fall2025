import sys


class Shape:

    def area(self): return 0
    def perimeter(self): return 0

# Ova' = rounded
# polygon = sided
class Polygon(Shape):
    def __init__(self, name, sides, side_dimensions):
        self.name = name
        self.sides = sides
        self.side_dimensions = side_dimensions
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) < 3: raise ValueError("Invalid Name")
        self.__name = value
    @property
    def sides(self): return self.__sides
    @sides.setter
    def sides(self, value):
        if not isinstance(value, int) and value < 3: raise ValueError("Invalid number of sides")
        self.__sides = value
    @property
    def side_dimensions(self): return self.__side_dimensions
    @side_dimensions.setter
    def side_dimensions(self, value):
        if isinstance(value, list):
            if not len(value) == self.sides: raise ValueError(f"You entered {len(value)} side dimension "
                                                              f"but {self.sides} side dimension were expected.")
            for v in value:
                if not isinstance(v, (int, float)) or v <= 0: raise ValueError(f"Side Dimension of {v} is invalid")
            self.__side_dimensions = value
        else: raise TypeError("Invalid type")
class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
    @property
    def length(self): return self.__length

    def _validate(self, value):
        if not isinstance(value, (int, float)): raise  ValueError("Invalid value!")
    @length.setter
    def length(self, value):
        self._validate(value)
        self.__length = value
    @property
    def width(self): return self.__width
    @width.setter
    def width(self, value):
        self._validate(value)
        self.__width = value

    def area(self): return self.length * self.width
    def perimeter(self): return 2 * (self.length + self.width)

# is a square a special kind of rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)
    @Rectangle.length.setter
    def length(self, value):
        Rectangle.length.__set__(self, value)
        Rectangle.width.__set__(self, value)
    @Rectangle.width.setter
    def length(self, value):
        Rectangle.width.__set__(self, value)
        Rectangle.length.__set__(self, value)


class Triangle(Polygon, Shape):

    def __init__(self, name, base, side1, side2):
        super().__init__(name, 3, [base, side1, side2])
    @Polygon.sides.setter
    def sides(self, value):
        Polygon.sides.__set__(self, value)
        if value != 3: raise ValueError("Triangle must have only 3 sides")

    def area(self): return (self.side_dimensions[0] * self.side_dimensions[2]) / 2
    def perimeter(self): return sum(self.side_dimensions)
try:
    s = Square("Square", 3)
    print(s.width)
    s.width = 4
    s.length = 2

    t = Triangle("Triangle", 2, 4, 6)
    print(t.area(), t.perimeter())
except Exception as e:
    print(e, file=sys.stderr)