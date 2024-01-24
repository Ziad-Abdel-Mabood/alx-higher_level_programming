#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = a / b
        print("Inside Result: {}".format(res))
    except(ZeroDivisionError):
        print("Inside Result: {}".format(res))
    finally:
        print("{} / {} = {}".format(a, b, res))
        return res
