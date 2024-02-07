#!/usr/bin/python3
"""function definition, writes a string to a text file"""


def write_file(filename="", text=""):
    """writes into file with UTF8 encoding"""
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
