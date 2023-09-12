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
        Initializes instance attributes
        Args:
            first_name: the first name of student
            last_name: the last name of student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method instance returning dict properties of object
        """
        if type(attrs) == list:  # check if it's a list
            for elem in attrs:
                if type(elem) != str:  # check if elements are srings
                    return (self.__dict__)

            dictionary = {}
            for num in range(len(attrs)):  # iterate through the list
                for item in self.__dict__:
                    if attrs[num] == item:
                        dictionary[item] = (self.__dict__[item])  # add item
            return (dictionary)

        return (self.__dict__)

    def reload_from_json(self, json):
        """
        replace all attributes of a Student instance
        """
        for item in json:
            self.__dict__[item] = json[item]
