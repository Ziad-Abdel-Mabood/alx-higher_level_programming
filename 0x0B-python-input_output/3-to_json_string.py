#!/usr/bin/python3
"""define to_json_string function"""


import json


def to_json_string(my_obj):
    """appends into file with UTF8 encoding"""
    return json.dumps(my_obj)
