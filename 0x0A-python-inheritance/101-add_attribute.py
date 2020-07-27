#!/usr/bin/python3

"""Class attribute
"""


def add_attribute(key, obj, name):
    """Add attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(key, obj, name)