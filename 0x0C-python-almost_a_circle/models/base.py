#!/usr/bin/python3
""" Base Class Module """


class Base:
    """ Base class
        nb_objects: manage id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor

            id : id number attr of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
