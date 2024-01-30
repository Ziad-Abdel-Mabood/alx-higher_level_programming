#!/usr/bin/python3
"""
defining class Rectangle
"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def width(self):
        return self.__width

    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)
