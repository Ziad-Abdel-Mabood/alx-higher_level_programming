#!/usr/bin/python3
def no_c(my_string):
    new_string = "".join(character for character in my_string if character != "c" and character != "C")
    return new_string
