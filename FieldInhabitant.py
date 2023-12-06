# Author: Vaishvik Brahmbhatt
# Date: 12/05/2023
# Description: A base class FieldInhabitant that is imported by all the classes in the project

class FieldInhabitant:
    def __init__(self, symbol):
        """
        Initialize the class with the given symbol
        :param symbol: Char: symbol of the instance
        """
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol
