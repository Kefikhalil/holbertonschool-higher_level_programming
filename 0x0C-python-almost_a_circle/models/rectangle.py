#!/usr/bin/python3

from models.base import Base
"""Class Rectangle
"""


class Rectangle(Base):
    """Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
