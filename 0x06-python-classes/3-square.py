#!/usr/bin/python3
"""
A python module that defines a class Square with private attributes
"""


class Square:
    """
    A class Square defining an attribute size
    """
    def __init__(self, size=0):
        """
        initializes an instance attribute with given value
        or zero if no value is given
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        finds the area of a square
        """
        return (self.__size ** 2)
