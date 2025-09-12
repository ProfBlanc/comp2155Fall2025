"""

Train

    ***************
    attributes
    ***************
    name            str
    num_cars         list[TrainCar]

    ***************
    actions
    ***************
    tostring that summarizes

TrainCar
    ***************
    attributes
    ***************
    car_number              int
    passengers              list[Passenger]
    
    ***************
    actions
    ***************
    add_passenger(Passenger p)
        add a passenger to the car
    remove_passenger(Passenger p)
    tostring that summarizes()
    save_passenger_info()
        write to file the TrainCar attributes
            write a file named "train_{traincar_car_number}.txt"
                content = car_number and full name of every passenger

Passenger
    ***************
    attributes
    ***************
    full_name


    ***************
    actions
    ***************
    tostring that summarizes



"""
class Passenger:
    def __init__(self, full_name):
        self.full_name = full_name
    @property
    def full_name(self): return self.__full_name
    @full_name.setter
    def full_name(self, value):
        if not isinstance(value, str) or len(value) < 3 or " " not in value:
            raise ValueError("Invalid full name")
        self.__full_name = value
    def __str__(self): return f"Passenger Name: {self.full_name}"

class TrainCar:
    def __init__(self, car_number):
        self.car_number = car_number
        self.__passengers = list()
    @property
    def car_number(self): return self.__car_number
    @car_number.setter
    def car_number(self, value):
        if not isinstance(value, str) or len(value) < 4:
            raise ValueError("Invalid car number")
        self.__car_number = value
    def add_passenger(self, p):
        if not isinstance(p, Passenger):
            raise TypeError("Incorrect Data Type passed. NOT a passenger")
        self.__passengers.append(p)
    def remove_passenger(self, p):
        if not isinstance(p, Passenger):
            raise TypeError("Incorrect Data Type passed. NOT a passenger")
        if p not in self.__passengers:
            raise ValueError(str(p) + " is NOT a passenger of the TrainCar " + self.car_number)
        
        self.__passengers.remove(p)
    def __str__(self): return f"TrainCar {self.car_number} has {len(self.__passengers)} passengers"
    def save_info(self):
        with open(f"{self.car_number}.txt", "w") as fo:
            fo.write(self.car_number)
            fo.write("\n")
            fo.write("Here are the list of passengers")
            fo.write("\n")
    def display_passengers(self):
        people = ""
        for p in self.__passengers:
            people += f"{p}\n"
        return people


p1 = Passenger("Ben Blanc")
p2 = Passenger("Mary Mary")
p3 = Passenger("John John")

tc = TrainCar("TC1234")
tc.add_passenger(p1)
tc.add_passenger(p2)
tc.add_passenger(p3)
print(tc)
tc.remove_passenger(p1)
print(tc)
print(tc.display_passengers())
