#!/usr/bin/python3
"""
module add_integer
this module has one method that takes two argument,
float or int. it converts the arguments to int
and then sum them up
"""


def add_integer(a, b=98):
    """returns addition of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
