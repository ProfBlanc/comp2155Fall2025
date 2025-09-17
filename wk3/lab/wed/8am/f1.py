import os.path

from wk2.lab.wed.early_morning_8am.f1 import Evaluation, Grade

class Course:
    def __init__(self, code, semester, year):
        self.code = code
        self.semester = semester
        self.year = year
        self.__evaluations = list()
    @property
    def code(self): return self.__code
    @code.setter
    def code(self, value):
        if not isinstance(value, str) and len(value) < 8: raise ValueError("Invalid course code")
        self.__code = value
    @property
    def semester(self): return self.__semester
    @staticmethod
    def valid_semesters(): return "Winter,Spring,Summer,Fall".split(",")
    @semester.setter
    def semester(self, value):
        if not isinstance(value, str) or value.title().strip() not in self.valid_semesters():
            raise ValueError("Invalid Semester")
        self.__semester = value
    @property
    def year(self): return self.__year
    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 2000 or value > 2050:
            raise ValueError("Invalid year")
        self.__year = value

    def add_evaluation(self, name:str, mark: int):
        if not isinstance(name, str) or not isinstance(mark, int): raise ValueError("Invalid evaluation data")
        self.__evaluations.append(Evaluation(name, Grade(mark)))

    def save(self):
        # year/semester/code
        root_path = os.path.join(str(self.year), self.semester, self.code)
        if not os.path.exists(root_path):
            os.makedirs(root_path)

        for e in self.__evaluations:
            with open(os.path.join(root_path, f"{e.name}.txt"), "w") as fo:
                fo.write(str(e.grade.percentage))


c = Course(code="comp2155", year=2025, semester="fall")
c.add_evaluation("mini-assignment_1", 90)
c.add_evaluation("quiz 1", 100)
c.save()