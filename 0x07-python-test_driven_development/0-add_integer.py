#!/usr/bin/python3

"""
class Add integers
"""


def add_integer(a, b=98):
    """
    Add two integers
    """    
    if a is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return b
    return int(a) + int(b)
