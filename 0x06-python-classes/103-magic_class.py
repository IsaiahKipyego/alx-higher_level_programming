#!/usr/bin/python3
"""
module that translates bytecode code
"""
import math


class MagicClass:
    """
    a class to calculate area and circumference of a circle
    """
    def __init__(self, radius=0):
        """
        initializes radius with zero
        """
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        gets area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        gets circumference of a circle
        """
        return 2 * math.pi * self.__radius
