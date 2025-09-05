import sys


class Grade:
    def __init__(self, percentage):
        self.percentage = percentage

    # enforce restrictions to class
    # decorator -> disguise a method as a _________
    @property
    def percentage(self): return self.__percentage
    @percentage.setter
    def percentage(self, value):
        if isinstance(value, int) and value >= 0 and value <= 100:
            self.__percentage = value
        else:
            raise ValueError("Invalid percentage")



class PassingGrade(Grade):
    @Grade.percentage.setter
    def percentage(self, value):
        Grade.percentage.__set__(self, value)
        if value < 50:
            raise ValueError("Not a passing grade")


try:
    g = Grade(int(input("Enter a grade: ")))
    print(g.percentage)
    pg = PassingGrade(int(input("Enter a passing grade: ")))
    print(pg.percentage)
except ValueError as e:
    print(e, file=sys.stderr)