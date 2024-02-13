#!/usr/bin/python3
""" Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """ Class represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


@property
def width(self):
    """width attr getter"""
    return self.__width


@width.setter
def width(self, input):
    """width attr setter"""
    self.assert_integer("width", input)
    self.__width = input


@property
def height(self):
    """height attr getter"""
    return self.__height


@height.setter
def height(self, input):
    """height attr setter"""
    self.assert_integer("height", input)
    self.__height = input


@property
def x(self):
    """ x attr getter"""
    return self.__x


@x.setter
def x(self, input):
    """ x attr setter"""
    self.assert_integer("x", input, coordinates=True)
    self.__x = input


@property
def y(self):
    """ y attr getter"""
    return self.__y


@y.setter
def y(self, input):
    """ y attr setter"""
    self.assert_integer("y", input, coordinates=True)
    self.__y = input


def assert_integer(self, attribute, input, coordinates=False):
    """ Method to make sure input is valid; integer and > 0"""
    if type(input) != int:
        raise TypeError(f"{attribute} must be an integer")
    if (not coordinates) and input <= 0:
        raise ValueError(f"{attribute} must be > 0")
    elif coordinates and input < 0:
        raise ValueError(f"{attribute} must be >= 0")
