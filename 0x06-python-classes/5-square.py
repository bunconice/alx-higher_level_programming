#!/usr/bin/python3

"""a class Square with private instance attribute:size"""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Check if value is an integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        """Check if value is greater than or equal to 0"""
        if value < 0:
            raise ValueError("size must be >= 0")

        """Assign value to the private attribute __size"""
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints to stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
