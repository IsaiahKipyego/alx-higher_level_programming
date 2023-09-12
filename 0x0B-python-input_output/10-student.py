#!/usr/bin/python3
"""
A module defining a class Student
"""


class Student:
    """
    A class defining a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize instance attributes
        Args:
            first_name: the first name of student
            last_name: the last name of student
            age: the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Instance method returning distinct properties of object
        """
        if type(attrs) == list:  # check if it's a list
            for elem in attrs:
                if type(elem) != str:  # check if elements are strings
                    return (self.__dict__)

            dictionary = {}
            for num in range(len(attrs)):  # iterate thro list
                for item in self.__dict__:
                    if attrs[num] == item:
                        dictionary[item] = (self.__dict__[item])  # add item
            return (dictionary)

        return (self.__dict__)
