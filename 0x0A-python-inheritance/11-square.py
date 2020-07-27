#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
"""rectangle class
"""


class Square(Rectangle):
    """Square
    """
    def __init__(self, size):
        """init
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
