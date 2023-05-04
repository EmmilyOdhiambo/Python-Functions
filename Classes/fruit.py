#Class Fruit
class Fruit:
    class attribute:
        is_fruit = True
    def __init__(self, name, color, taste):
# instance variables
        self.name = name
        self.color = color
        self.taste = taste
    def describe(self):
            print(f"This {self.color} {self.name} tastes {self.taste}.")
    def eat(self):
        print(f"You eat the {self.name}.")
    def rot(self):
        print(f"The {self.name} tastes sweetest.")

