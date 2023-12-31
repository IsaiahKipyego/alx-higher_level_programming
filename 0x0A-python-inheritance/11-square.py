#!/usr/bin/python3
"""
A module that contains a class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class inherits properties from the Rectangle class
    """
    def __init__(self, size):
        """
        Initializes square class with its properties
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        gets area of the square
        """
        return super().area()

    def __str__(self):
        """
        magic method returns a formated string
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
