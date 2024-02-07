#!/usr/bin/python3
"""function definition, appends a string to a text file"""


def append_file(filename="", text=""):
    """appends into file with UTF8 encoding"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
