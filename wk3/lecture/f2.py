class Mother:
    def __init__(self, a, b): pass
    def caring(self):
        return "Mom cares for you"
    def talking(self, topic):
        return "Here's what I thing about " + topic

class Father:
    def __init__(self, a, b, c): pass
    def caring(self): return "Father cares for you"
    def taking_care(self): return "Father takes care of child"
    def educate(self, subject): return f"Here's what I know about " + subject

class Child(Mother, Father):
    def sleeping(self, duration):
        return f"Child slept for {duration} hours"
    def playing(self, location): return "Child is playing " + location


mom = Mother(1, 2)
dad = Father(1, 2, 3)
me = Child()
print(me.caring())