class Grade:
    def __init__(self, percentage: int) -> None:
        self.percentage = percentage

    # decorator: disguise a method as something else
    @property
    def percentage(self):
        return self.__percentage
    @percentage.setter
    def percentage(self, value):
        if isinstance(value, int) and value >= 0 and value <= 100:
            self.__percentage = value
        else:
            raise ValueError("Percentage must be between 0 and 100")

class Student:
    def __init__(self, name:str, age:int)-> None:
        self.name = name
        self.age = age
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name is not string")
    @property
    def age(self): return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 1 and value <= 65: self.__age = value
        else: raise ValueError("Age is not valid")


class PassingGrade(Grade):
    @Grade.percentage.setter
    def percentage(self, value: int)->None:
        Grade.percentage.__set__(self, value)
        if value < 50: raise ValueError("This is NOT a passing grade")


pg = PassingGrade(100)
print(pg.percentage)
# mg = Grade(11)
# print(mg.percentage)
