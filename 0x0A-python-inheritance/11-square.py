#!/usr/bin/python3
""Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """Initializer"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Square area"""
        return self.__size**2

    def __str__(self):
        """def"""
        return "[Square] {}/{}".format(self.__size, self.__size)