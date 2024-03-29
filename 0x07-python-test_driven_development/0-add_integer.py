#!/usr/bin/python3
"""
Project 0x07

task 0 :
write a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """ adds two ints"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
