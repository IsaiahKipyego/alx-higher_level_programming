#!/usr/bin/python3
"""
A module defining a Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square inheriting from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Sets properties of square using super class(Rectangle)
        Args:
            size (int): size of length and width of the square
            x (int):  x value
            y (int):  y value
            id: id of the new object
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """
        A getter function for width and height attributes
        Return:
            value of on side of the square
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        A setter function for width and height of the object
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overloads __str__ and produces a formatted output for the object
        Return:
            formatted output specific to the object
        """
        out = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.width)
        return (out)

    def update(self, *args, **kwargs):
        """
        Updates values of a given object with given values
        Args:
            args (optional): non keyworded arguments
            kwargs (optional): keyworded arguments
        """
        if args and len(args) != 0:
            pos = 0
            for arg in args:
                if pos == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif pos == 1:
                    self.size = arg
                elif pos == 2:
                    self.x = arg
                elif pos == 3:
                    self.y = arg
                pos += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Creates a dictionary representation of an object
        Return:
            object representation as a dictionary
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
