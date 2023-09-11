#!/usr/bin/python3
"""
A module that contains a function  that adds attributes to objects
"""


def add_attribute(obj, name, prop):
    """
    a function adds new attributes to an object or class
    Args:
        obj: the object to add
        name: the attribute name
        prop: the property of attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, prop)
