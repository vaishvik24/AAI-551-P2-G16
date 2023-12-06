#Name: Kush Patel

from Creature import Creature  # Importing the Creature class

class Rabbit(Creature):  # Defining a class named Rabbit, inheriting from Creature
    def __init__(self, x, y):  # Initializing the Rabbit class with parameters x and y
        super().__init__(x, y, "R")  # Calling the constructor of the superclass Creature with the symbol "R"
