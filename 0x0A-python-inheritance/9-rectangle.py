#!/usr/bin/python3

"""
class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry
    """
    def area(self):
        """area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle
    """
    def __init__(self, width, height):
        """init
        """
        BaseGeometry.__init__(self)
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """area
        """
        return self.__width * self.__height

    def __str__(self):
        """str
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)