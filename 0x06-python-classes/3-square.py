#!/usr/bin/python3
""" Square class """


class Square:
    """ an square class; defined by its size"""
    def __init__(self, size=0):
        """ initializing the square optionally with the size attr"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (size * 2)
