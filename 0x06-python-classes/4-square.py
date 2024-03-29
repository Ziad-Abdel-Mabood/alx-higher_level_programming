#!/usr/bin/python3
""" Square class """


class Square:
    """ an square class; defined by its size"""
    def __init__(self, size=0):
        """Constructor Method

        Args:
            size: length of the side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Property getter

        Returns:
            square size i.e side length.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter

        changes size value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square.

        Returns:
            area of the square calculated by
            squaring the side length.
        """
        return self.__size ** 2
