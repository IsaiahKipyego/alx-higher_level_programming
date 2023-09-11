#!/usr/bin/python3
"""
module with function ``print_square`` that prints a square using "#"
and accepts integer values
"""


def print_square(size):
    """
    function that prints a square using "#"
    Args:
        size: the size of square
    Return:
        No return value
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
