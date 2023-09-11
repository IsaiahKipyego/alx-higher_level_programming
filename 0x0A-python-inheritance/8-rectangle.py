#!/usr/bin/python3
"""
contains a class without area implementation
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        """
        a method initialises object attributes
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
