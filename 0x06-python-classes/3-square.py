#!/usr/bin/python3
""" Square class """


class Square:
    """ an square class; defined by its size"""
    def __init__(self, size=0):
        """Constructor Method

        Args:
            size: length of the side of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square.

        Returns:
            area of the square calculated by
            squaring the side length.
        """
        return self.__size ** 2
