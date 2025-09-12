"""
Grade:
    percentage
    letter
    tostring method: summarize Grade => percentage % (letter)

Evaluation
    name        string
    grade       Grade
    tostring method: summarize name and grade of evaluation
    save()      write the data to the file system
                write a file named {name}.txt
                        content = grade % & grade letter
    

To-Do as Bonus Exercise (NOT for marks)

Create a Course
    code        string      8 chars: first 4 are letters, next 4 are numbers
    semester    string      one of X values: Fall,Winter,Spring
    evaluations Evaluation  name and Grade

"""
class Grade:
    def __init__(self, percent):
        self.percent = percent
    @property
    def percent(self): return self.__percent
    @percent.setter
    def percent(self, value):
        if isinstance(value, int) and value >= 0 and value <= 100:
            self.__percent = value
            
            letter = 'F'
            if value >= 90: letter = "A+"
            elif value >= 80: letter = "A"
            elif value >= 70: letter = "B"
            elif value >= 60: letter = "C"
            elif value >= 50: letter = "D"
            
            self.__letter = letter
        else: raise ValueError("Invalid grade percentage")
    
    @property
    def letter(self): return self.__letter
    
    def __str__(self): return f"{self.percent}% ({self.letter})"

g = Grade(90)
print(g)
g.percent = 70
print(g)

class Evaluation:
    def __init__(self, name: str, mark: int) -> None:
        self.name = name
        self.mark = Grade(mark)
    @property
    def name(self): self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
        else: raise ValueError("Invalid Name")
        
    def __str__(self): return f"Name: {self.name}, Grade: {self.mark}"
    def save(self):
        with open(f"{self.name}.txt", "w") as fo:
            fo.write(str(self.mark))

name = input("Enter an evaluation name: ")
mark = int(input("Enter an evaluation mark: "))

e = Evaluation(name=name, mark=mark)
print(e)
e.save()
