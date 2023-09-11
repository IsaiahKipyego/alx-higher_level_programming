#!/usr/bin/python3
"""
contains a class without area implementation
"""


class BaseGeometry:
    """
    base class of a geometry class
    """
    def area(self):
        """
        raises an error exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates an int or value provided
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
