#!/usr/bin/python3

"""a class Square with private instance attribute: size"""


class Square:
    """private instance attribute: size"""
    def __init__(self, size=0):
        """check if size is an integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """check if size is greater than zero"""
        if size < 0:
            raise ValueError("size must be >= 0")

        """Assign size to the private attribute __size"""
        self.__size = size

    def area(self):
        """return area of the Square"""
        return self.__size ** 2
