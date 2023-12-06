"""
Author: Hemil Patel (20013017)
Date: 2nd dec 2023
Description: Captain which is a subclass of Creature and the class takes x and y coordinates of the captain 
and symbol "V" which represents Captain on the grid. It also has a method add_veggie that is used to add the list 
of veggie objects. 
"""

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._veggies_collected = []

    def add_veggie(self, veggie):
        self._veggies_collected.append(veggie)

    def get_veggies_collected(self):
        return self._veggies_collected

    def set_veggies_collected(self, veggies_collected):
        self._veggies_collected = veggies_collected
