#!/usr/bin/python3
def safe_print_integer(value):
    n = False
    try:
        print("{:d}".format(value))
        n = True
    except ValueError:
        pass
    return n
