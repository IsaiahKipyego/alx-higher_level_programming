#!/usr/bin/python3
"""
module defining class Student
"""


class Student:
    """
    class defining a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes instance attributes
        Args:
            first_name: the first name of student
            last_name: the last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Instance method returns dict properties of the object
        """
        return (self.__dict__)
