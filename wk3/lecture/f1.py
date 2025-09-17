class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def __str__(self): return f"Person's name is {self.name}" \
        f" and works as a {self.job}"

    def transform(self):
        return f"{self.name} cannot transform, as {self.name} is only a Person"

ck = Person("Clark Kent", "Reporter")
print(ck)

class SuperHero(Person):
    def __init__(self, name, job, hero_name, hero_power):
        # self.name = name
        # self.job = job
        super().__init__(name, job)
        #Person.__init__(self, name, job)

        self.hero_name = hero_name
        self.hero_power = hero_power
    def __str__(self):

        return super().__str__() + f". Hero Name is {self.hero_name}"\
                f" and Hero Power is {self.hero_power}"

    def transform(self):
        return f"{self.name} is transforming into {self.hero_name}"

sm = SuperHero(name="Clark Kent", job="Reporter",
               hero_name="Superman", hero_power="Flying")
print("*" * 20)
print(sm)
print(ck.transform())
print(sm.transform())