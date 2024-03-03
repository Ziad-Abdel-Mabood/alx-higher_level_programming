#!/usr/bin/python3
""" say my name function module """


def say_my_name(first_name, last_name=""):
    """ prints My name is then the first and last names
    Args:
        first_name: first name of the user
        last_name:  last name of the user, empty by default
    Return: nothing
    Raises:
        TypeError: if first name is not a string
        TypeError: if last_name is not a string
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
