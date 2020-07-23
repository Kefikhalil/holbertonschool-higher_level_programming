#!/usr/bin/python3

"""Integer validator"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer
            name (str): the given name
            value (int): the given integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
