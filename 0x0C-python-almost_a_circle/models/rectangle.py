#!/usr/bin/python3
"""
A module defining a class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    A class defining a Rectangle with it's properties
    inherits attributes of the class 'Base'
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize rectangle with it's properties
         Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): position horizontally
            y (int): position vertically
            id: id of the object
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        A getter method for width attribute
        Return:
             width of object
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        A setter method for width property
        Args:
            value: value of width
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        A getter method for height property
        Return:
            value of the height property of the object
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        A setter method for height property
        Args:
            value: value of height attributes
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        A getter method for the x attribute
        Return:
          value of x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        A setter method for the x attribute
        Args:
            value: value of x to be set
        """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        A getter method for y property
        Return:
            value of y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        A setter method for y attribute
        Args:
            value: value of the y attribute
        """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calcualate area of the object(Rectangle)
        Return:
             computed area
        """
        return (self.__height * self.width)

    def display(self):
        """
        Display rectangle using the '#' symbol
        Prints rectangle on stdout
        """
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for y in range(self.__y):
                print()
            for row in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

    def __str__(self):
        """
        Overloads __str__ and return formated output of the Rectangle
        Return:
            formatted output
        """
        out = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                      self.__y, self.__width,
                                                      self.__height)
        return (out)

    def update(self, *args, **kwargs):
        """
        update values of an object given new values to set the object
        only sets args values if both optional arguments exist
        Args:
            args (optional): non keyworded arguments
            kwargs (optional): key worded arguments
        """
        if (args and len(args) != 0):
            pos = 0
            for arg in args:
                if pos == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x,
                                      self.y)
                    else:
                        self.id = arg
                elif pos == 1:
                    self.width = arg
                elif pos == 2:
                    self.height = arg
                elif pos == 3:
                    self.x = arg
                elif pos == 4:
                    self.y = arg
                pos += 1
        elif (kwargs and len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height,
                                      self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Sets the values of the object into a dictionary representation
        Return:
            dictionary containing all the attributes of the object
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
