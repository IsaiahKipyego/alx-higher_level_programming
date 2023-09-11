#!/usr/bin/python3
"""
module with a function that prints first and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    takes two string parameters and prints out the name
    """

    # checks if arguments are strings
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
