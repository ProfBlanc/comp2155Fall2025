import csv
class Person:
    def __init__(self, name, age):
        self.name = name
        self. age = age
    def __str__(self): return f"{self.name} ({self.age})"

people = list()
people.append(Person("John", 20))
people.append(Person("Mary", 21))
people.append(Person("Jill", 22))

data = list()  # data to write to file
fields = "name,age".split(",")  # represent column names
for person in people:
    row = dict.fromkeys(fields)
    row[fields[0]] = person.name
    row[fields[1]] = person.age

    data.append(row)

with open("my.csv", "w") as fo:
    writer = csv.DictWriter(fo, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(data)

