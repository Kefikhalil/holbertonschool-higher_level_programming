#!/usr/bin/python3

"""CLass Rectangle 
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle
    """

    def __init__(self, width, height):
        """
        init
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
