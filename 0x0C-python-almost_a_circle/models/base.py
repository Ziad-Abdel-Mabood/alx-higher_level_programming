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

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string representation of  list_objs to a file"""
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open("{}.json".format(cls.__name__), w, encoding="utf-8") as file:
            file.write(json_string)
