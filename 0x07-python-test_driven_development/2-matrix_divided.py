#!/usr/bin/python3
"""
Module 2-matrix_divided
contains method that divides all elements of a matrix
by a given number
"""


def matrix_divided(matrix, div):
    """
    Args:
    matrix - a list of lists of integers or floats

    div : The divisor is an integer or float and != zero.

    Returns:
    list: A new matrix with elements divided by 'div',
    rounded to 2 decimal places
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
