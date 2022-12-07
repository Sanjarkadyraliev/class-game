# class Heroes():
#     def __init__(self,name, hp, power, category):
#         self.name = name
#         self.hp = hp
#         self.power = power
#         self.category = category
#
# class Melee(Heroes):
#     def __init__(self, name, hp, power, category, melee):
#         super().__init__(name, hp, power,category)
#         self.melee = melee
# class Range(Heroes):
#     def __init__(self, name, hp, power, category, range):
#         super().__init__(name, hp, power, category)
#         self.range = range
#
# hero1 = Range("Zeus", 750, 50, "intell", "range")
# hero2 = Melee("Phantom", 600, 65, "Agility","melee")
import time
class Car:
    def __init__(self, model, weight, speed, category):
        self.model = model
        self.weight = weight
        self.speed = speed
        self.category = category

class Detail_info(Car):
    def __init__(self, model, weight, speed, category, color, door):
        super().__init__(model, weight, speed, category)
        self.color = color
        self.door = door

    def drive(self):
        print("this car is", self.model, "his weight is", self.weight)

class Made_in(Car):
    def __init__(self, model, weight, speed, category, country):
        super().__init__(model,weight, speed, category)
        self.country = country

    def check(self):
        print(f"this car made in {self.country}")

honda = Detail_info("Honda", 2000, 150, "sedan", "black", 4)
mazda = Made_in("Mazda",1450, 145, "sedan", "Japan")
honda.drive()
mazda.check()

def racing(distance, mass_coef):
    new_distance = distance
    while distance > 0 and new_distance > 0:
        time.sleep(1)
        print(f"this distance is for {distance}")
        print(f"this distance is for {new_distance}")
        distance -= honda.speed - (honda.weight * mass_coef)
        new_distance -= mazda.speed -(mazda.weight * mass_coef)
    if distance > new_distance:
        print(f"winner is {mazda.model}")
    elif distance < new_distance:
        print(f"winner is {honda.model}")
    else:
        print(f"friendship")

racing(1000, 0.01)

