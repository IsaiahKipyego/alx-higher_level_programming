#!/usr/bin/python3
"""
module containing class Rectangle
"""


class Rectangle:
    """
    A class Rectangle which defines a Rectangle with two properties
    whose properties are it's width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initializes private attributes width and height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        getter method for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method for height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter method for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public instance method,for finding area of the Rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        public instance method, finds perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
        returns the rectangle printed with a '#' character
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return (string)
        for x in range(self.__height):
            string += "#" * self.__width + "\n"

        return (string[:-1])

    def __repr__(self):
        """
        returns a string representation of rectangle
        can be used to create a new instance using eval()
        """
        str_tuple = (self.__width, self.__height)
        string = "Rectangle" + str(str_tuple)
        return (string)

    def __del__(self):
        """
        print message when instance is deleted
        """
        del self
        print("Bye rectangle...")
