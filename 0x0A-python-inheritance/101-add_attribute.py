#!/usr/bin/python3

"""Class attribute
"""


def add_attribute(obj, key, name):
    """Add attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, name)
