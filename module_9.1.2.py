# Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car.

# 1.

'''class Car:
    def __init__(self, reg_num, max_speed, cur_speed = 0, trav_distance = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.trav_distance = trav_distance
    def info(self):
        print(f"Reg.Number: {self.reg_num}\nMax speed: {self.max_speed} km/h")
        print(f"Current speed: {self.cur_speed}\nTrav_distance: {self.trav_distance}\n")

car1 = Car("abc-123", 300)
car2 = Car("ste-123", 50)

car1.info()
car2.info()'''
import random

# Extend the program by adding an accelerate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed. The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car.
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

# 2.

'''class Car:
    def __init__(self, reg_num, max_speed, acceleration, cur_speed = 0, trav_distance = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.cur_speed = cur_speed
        self.trav_distance = trav_distance
    def speed(self):
        self.cur_speed = self.cur_speed + self.acceleration
        if self.cur_speed <= 0:
            self.cur_speed = 0
    def info(self):
        print(f"Reg.Number: {self.reg_num}\nMax speed: {self.max_speed} km/h")
        print(f"Current speed: {self.cur_speed} km/h\nTrav_distance: {self.trav_distance}\n")

car1 = Car("abc-123", 300, -10)
car2 = Car("ste-123", 50, 24)

car1.speed()
car2.speed()

car1.info()
car2.info()
'''
# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.

# 3.

'''class Car:
    def __init__(self, reg_num, max_speed, acceleration, time = 0, cur_speed = 0, trav_distance = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.time = time
        self.cur_speed = cur_speed
        self.trav_distance = trav_distance
    def speed(self):
        self.cur_speed = self.cur_speed + self.acceleration
        if self.cur_speed <= 0:
            self.cur_speed = 0

    def drive(self, time):
        self.time = time
        self.trav_distance = self.trav_distance + (self.time * self.cur_speed)

    def info(self):
        print(f"Reg.Number: {self.reg_num}\nMax speed: {self.max_speed} km/h")
        print(f"Current speed: {self.cur_speed} km/h\nTrav_distance: {self.trav_distance}\n")

car1 = Car("abc-123", 300, -10)
car2 = Car("ste-123", 50, 24)

car1.speed()
car2.speed()

car1.drive(2)
car2.drive(1.5)

car1.info()
car2.info()'''

# Now we will program a car race.
# The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
# One per every hour of the race, the following operations are performed:
#
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accelerate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.

# 4.
import random

class Car:
    def __init__(self, reg_num, max_speed, time = 0, cur_speed = 0, trav_distance = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        #self.acceleration = acceleration
        self.time = time
        self.cur_speed = cur_speed
        self.trav_distance = trav_distance

    '''def create_cars(self):
        cars = []
        for i in cars:
            if len(cars) < 10:
                cars.append += 1'''

    def speed(self):
        a = random.randint(-10, 15)
        self.cur_speed += a
        if self.cur_speed <= 0:
            self.cur_speed = 0
        elif self.cur_speed >= self.max_speed:
            self.cur_speed = self.max_speed
        #else:
        #    print("Error in speed :b")

    def drive(self, time):
        self.time = time
        self.trav_distance = self.trav_distance + (self.time * self.cur_speed)

    def info(self):
        print(f"Reg.Number: {self.reg_num}\nMax speed: {self.max_speed} km/h")
        print(f"Current speed: {self.cur_speed} km/h\nTrav_distance: {self.trav_distance}\n")

def create_cars():
    cars = []
    #max_speed = random.randint(100, 200)
    for i in range(1,11):
        a_car = f"ABC-{i}"
        cars.append(Car(a_car, max_speed = random.randint(100, 200)))
    return cars

def race(cars):
    time = 0
    while True:
        time += 1
        for car in cars:
            car.speed()
            car.drive(1)
            if car.trav_distance >= 10000:
                print("---------------------------")
                print(f"\n   Winner is {car.reg_num}\n")
                print("---------------------------")
                return

def table(cars):
    print("▓ Reg_Num: ▓ Trav_distance: (km) ▓ Max_Speed: (km/h) ▓ Current_speed: (km/h) ▓")
    print("------------------------------------------------------------------------------")
    for car in cars:
        print(f"┊  {car.reg_num:<7} ┊    {car.trav_distance:<16} ┊  {car.max_speed:<16} ┊   {car.cur_speed:<19} ┊")
    print("------------------------------------------------------------------------------")
cars = create_cars()
race(cars)
table(cars)

# The pretty tableÖ https://www.w3schools.com/python/ref_string_format.asp
# ▓ ┊ source for the future: TextSymbols.net


                #!!!!!!!!!

#car1 = Car("abc-123", 300, -10)
#car2 = Car("ste-123", 50, 24)

'''car1.speed()
car2.speed()

car1.drive(2)
car2.drive(1.5)'''

'''car1.info()
car2.info()
'''