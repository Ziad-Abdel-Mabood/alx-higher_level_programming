#!/usr/bin/python3
""" Base Class Module """
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ serializes a list of dicts and returns the json string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
