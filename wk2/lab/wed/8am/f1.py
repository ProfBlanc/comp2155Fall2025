from wk1.lab.wed.early_morning_8am.f1 import Grade

class Evaluation:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self.__name = value
    @property
    def grade(self): return self.__grade
    @grade.setter
    def grade(self, value):
        if not isinstance(value, Grade): raise ValueError("Invalid Grade")
        self.__grade = value
    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade.percentage}%"

    def save(self):
        with open(f"{self.name}.txt", "w") as fo:
            fo.write(self.__str__())

exam = Evaluation("Mid-Term Exam", Grade(90))
print(exam)
exam.save()