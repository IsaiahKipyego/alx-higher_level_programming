#!/usr/bin/python3
"""
contains a class without an area implementation
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
