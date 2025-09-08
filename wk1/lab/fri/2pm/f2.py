class Grade:
    def __init__(self, percentage):
        self.percentage = percentage

    @property
    def percentage(self):
        return self.__percentage

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
            raise ValueError("NOT a passing grade")


try:
    g = PassingGrade(int(input("enter a grade: ")))
    print(g.percentage)
except ValueError as e:
    print(e)
