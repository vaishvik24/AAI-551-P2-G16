# Author: Vaishvik Brahmbhatt
# Date: 12/05/2023
# Description: A Creature class that contains its position and its symbol

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
        Initialize the co-ordinate for creature with given symbol
        :param x: int: x axis position
        :param y: int: y axis position
        :param symbol: Char: type of symbol
        """
        super().__init__(symbol)
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y
