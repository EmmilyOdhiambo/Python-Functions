# #Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

class Car:
    # class Car:
        class attribute:
            wheels = 4
        def __init__(self, make, model, color):
    #instance variables
            self.make = make
            self.model = model
            self.color = color
        def start_engine(self):
            print(f"The {self.color} {self.make} {self.model} has started its engine.")

        def drive(self):
            print(f"The {self.color} {self.make} {self.model} is driving.")

        def stop(self):
            print(f"The {self.color} {self.make} {self.model} has stopped at 72km/h.")
