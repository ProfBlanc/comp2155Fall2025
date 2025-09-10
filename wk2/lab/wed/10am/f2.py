import os

from f1 import Evaluation, Grade

class Course:
    def __init__(self, code, year, semester):
        self.code = code
        self.year = year
        self.semester = semester
        self.__evaluations = list()

    # add decorators for code, year, semester
    @property
    def semester(self): return self.__semester
    @semester.setter
    def semester(self, value):
        # create a static method outlining list of valid semester. Call this method
        # to validate semester value (Look at wk2 lecture code for help)
        if isinstance(value, str) and value[0].lower() in "w,f,s".split(","):
            self.__semester = value
        else:
            raise ValueError("Invalid Semester value")
    def add_evaluation(self, value):
        if isinstance(value, Evaluation):
            self.__evaluations.append(value)
    def save(self):
        path = f"{self.year}/{self.semester}/{self.code}"
        os.makedirs(path, exist_ok=True)  # year/semester/code        # 2025/fall/comp2155
        for evaluation in self.__evaluations:
            with open(f"{path}/{evaluation.name}.txt", "w") as fo:
                fo.write(str(evaluation))

c = Course(code="comp2155", year="2025", semester="fall")

c.add_evaluation(Evaluation(name="assignment1", grade=Grade(90)))
c.add_evaluation(Evaluation(name="finalexam", grade=Grade(95)))

c.save()