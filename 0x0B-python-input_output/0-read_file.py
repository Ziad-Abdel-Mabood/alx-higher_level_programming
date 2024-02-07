#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """reads filename with utf-8"""
    with open(filename, 'r', encoding="utf-8") as file:
        data = file.read()
    print(data, end="")
