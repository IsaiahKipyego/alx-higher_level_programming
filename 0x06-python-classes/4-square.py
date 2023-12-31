#!/usr/bin/python3
"""
A python module that defines a class Square with private attributes
"""


class Square:
    """
    A class Square that defines an attribute size
    """
    def __init__(self, size=0):
        """
        initializes an instance attribute with given value
        or zero if no value is given
        """
        self.size = size

    @property
    def size(self):
        """
        getter function to get the value of private attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter function to set the value of the private attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        finds the area of a square
        """
        return (self.__size ** 2)
