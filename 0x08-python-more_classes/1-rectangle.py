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
        return self.width

    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    def height(self):
        return self.height

    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
