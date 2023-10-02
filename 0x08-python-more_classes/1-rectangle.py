#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """Rectangle class with private instance attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """checks if value is not an int"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """checks if value is less than zero"""
        if value < 0:
            raise ValueError("width must be >= than 0")
        """assign value to private attribute width"""
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """checks if value is not an int"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """checks if value is less than zero"""
        if value < 0:
            raise ValueError("height must be >= than 0")
        """assign value to private attribut height"""
        self.__height = value
