#!/usr/bin/python3
"""Square #1"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """Initialise"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Square area"""
        return self.__size**2
