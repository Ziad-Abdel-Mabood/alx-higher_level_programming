#!/usr/bin/python3
""" Module of Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class representation of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns string info about square instance"""
        return '[{}] ({}) {}/{} - {}'.\
               format(type(self).__name__, self.id, self.x, self.y,
                      self.height)

    @property
    def size(self):
        """ side length of the square"""
        return self.width

    @size.setter
    def size(self, input):
        self.width = input
        self.height = input

    def update(self, *args, **kwargs):
        """ updates instance attr"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __update(self, id=None, size=None, x=None, y=None):
        """ updates attributes depending on given input"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """ returns the dict representation of a Rectangle class"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
