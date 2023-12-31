#!/usr/bin/python3
"""
python  module that defines a class Square with private attributes
"""


class Square:
    """
    class Square that defines an attribute size
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
        getter function to get value of private attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter function to set value of private attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        finds area of a square
        """
        return (self.__size ** 2)

    def __lt__(self, sqr):
        """
        compares with less than operator
        """
        return self.area() < sqr.area()

    def __le__(self, sqr):
        """
        compares with less than or equal to operator
        """
        return self.area() <= sqr.area()

    def __eq__(self, sqr):
        """
        compares with equality operator
        """
        return self.area() == sqr.area()

    def __ne__(self, sqr):
        """
        compares with not equal to operator
        """
        return self.area() != sqr.area()

    def __gt__(self, sqr):
        """
        compares with greater than operator
        """
        return self.area() > sqr.area()

    def __ge__(self, sqr):
        """
        compares with greater than or equal to operator
        """
        return self.area() >= sqr.area()
