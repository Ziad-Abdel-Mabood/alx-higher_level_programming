#!/urs/bin/python3
""" Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """ Class represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


@property
def width(self):
    """width attr getter"""
    return self.__width


@width.setter
def width(self, input):
    """width attr setter"""
    self.width = input


@property
def height(self):
    """height attr getter"""
    return self.height


@height.setter
def height(self, input):
    """height attr setter"""
    self.height = input


@property
def x(self):
    """ x attr getter"""
    return self.x


@x.setter
def x(self, input):
    """ x attr setter"""
    self.x = input


@property
def y(self):
    """ y attr getter"""
    return self.x


@y.setter
def y(self, input):
    """ y attr setter"""
    self.y = input
