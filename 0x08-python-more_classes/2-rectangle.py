#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """defining the Rectangle class"""
    def __init__(self, width=0, height=0):
        """initializing the class
        Arg:
            width:width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
