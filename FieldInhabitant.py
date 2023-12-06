# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:19:30 2023

@author: hemil
"""

class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol
