#!/usr/bin/python3
"""
module that contains function ``matrix_divided`` that divides a matrix with a
given parameter
takes two arguments- matrix and divisor
"""


def matrix_divided(matrix, div):
    """
    function divides a matrix with given divisor
    Args:
        matrix: matrix to divide
        div: divisor
    Return:
        returns divided matrix, raises an exception if error is encountered
    """

    type_msg = "matrix should be a matrix of integers/floats"
    size_msg = "Each row of the matrix must have the same size"

    if type(matrix) != list or not matrix:  # if not a list or empty list
        raise TypeError(type_msg)

    size = 0
    for elem in matrix:
        if not elem:  # if element is empty - no values inside
            raise TypeError(type_msg)

        if type(elem) != list:  # if element is not a list
            raise TypeError(type_msg)

        if size != 0 and len(elem) != size:  # elements are of different sizes
            raise TypeError(size_msg)
        size = len(elem)

        for items in elem:  # check if each item is a float or int
            if type(items) not in (int, float):
                raise TypeError(type_msg)

    if type(div) not in (int, float):  # if divisor is not an int or float
        raise TypeError("div must be a number")

    if div == 0:  # division by zero
        raise ZeroDivisionError("division by zero")

    # perform the operation
    value = list(map(lambda row: list(map(lambda col: round(col / div, 2),
                                          row)), matrix))

    return (value)
