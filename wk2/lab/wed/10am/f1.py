from wk1.lab.wed.late_morning_10am.f1 import Grade
class Evaluation:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name is not a string')
        self.__name = value

    @property
    def grade(self): return self.__grade
    @grade.setter
    def grade(self, value):
        if not isinstance(value, Grade):
            raise TypeError('Not a valid grade')
        self.__grade = value

    def save(self):
        with open(f"{self.name}.txt", "w") as fo:
            fo.write(self.__str__())
            fo.write("\n")
            fo.write(str(self))
    def __str__(self): return f"Name: {self.name}, Grade: {self.grade.percentage}%"

midterm = Evaluation(name="MidtermExam", grade=Grade(90))
print(midterm)
midterm.save()

e_name = input("Enter evaluation name: ")
e_grade = int(input("Enter evaluation grade: "))

e = Evaluation(name=e_name, grade=Grade(e_grade))
print(e)
e.save()
