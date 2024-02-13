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

    def __str__(self):
        """returns string info of this rectangle object"""
        return '[{}] ({}) {}/{} - {}/{}'.\
               format(type(self).__name__, self.id, self.x, self.y,
                      self.width, self.height)

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

    def update(self, *args, **kwargs):
        """ updates instance attr"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
        
    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """ updates attributes depending on given input"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """ returns the dict representation of a Rectangle class"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
