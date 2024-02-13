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
        self.assert_integer("width", input, False)
        self.__width = input

    @property
    def height(self):
        """height attr getter"""
        return self.__height

    @height.setter
    def height(self, input):
        """height attr setter"""
        self.assert_integer("height", input, False)
        self.__height = input

    @property
    def x(self):
        """ x attr getter"""
        return self.__x

    @x.setter
    def x(self, input):
        """ x attr setter"""
        self.assert_integer("x", input)
        self.__x = input

    @property
    def y(self):
        """ y attr getter"""
        return self.__y

    @y.setter
    def y(self, input):
        """ y attr setter"""
        self.assert_integer("y", input)
        self.__y = input

    def assert_integer(self, attribute, input, equal=True):
        """ Method to make sure input is valid; integer and > 0"""
        if type(input) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if equal and input < 0:
            raise ValueError("{} must be >= 0".format(attribute))
        elif not equal and input <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """ calculates area of rectangle"""
        return self.height * self.width

    def display(self):
        """ prints in stdout a representation of the rectangle"""
        graphic = '\n' * self.y + \
                  (' ' * self.x + '#' * self.width + '\n') * self.height
        print(graphic, end='')
