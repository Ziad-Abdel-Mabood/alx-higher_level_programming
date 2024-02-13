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
               format(type(self.__name__), self.id, self.x, self.y,
                      self.height)
