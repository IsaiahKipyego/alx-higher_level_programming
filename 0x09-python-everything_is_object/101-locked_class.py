#!/usr/bin/python3
"""
a Module that contains a class preventing user from dynamically creating
a new instance attribute of a class
"""


class LockedClass:
    """
    A class preventing dynamic creation of instance attributes
    """
    __slots__ = ['first_name']

    def __init__(self, value=""):
        """
        initializes first name variable with an optional value
        """
        self.first_name = value
