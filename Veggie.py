# Author: Kush Patel
# Date: 09/03/2023
# Description: simple program that creates a layout for Veggie class

from FieldInhabitant import FieldInhabitant  # Importing necessary module


class Veggie(FieldInhabitant):  # Defining a class named Veggie, inheriting from FieldInhabitant
    def __init__(self, name, symbol, points):  # Initializing the Veggie class with parameters
        super().__init__(symbol)  # Calling the constructor of the superclass FieldInhabitant
        self._name = name  # Initializing the name attribute
        self._points = points  # Initializing the points attribute

    def get_name(self):  # Method to retrieve the name attribute
        return self._name

    def set_name(self, name):  # Method to set the name attribute
        self._name = name

    def get_points(self):  # Method to retrieve the points attribute
        return self._points

    def set_points(self, points):  # Method to set the points attribute
        self._points = points

    def __str__(self):  # Method to return a string representation of the object
        return f"Symbol: {self.get_symbol()}, Name: {self.get_name()}, Points: {self.get_points()}"
