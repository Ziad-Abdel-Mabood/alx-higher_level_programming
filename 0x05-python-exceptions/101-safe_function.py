#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(args)
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        result = None
    return result
