#!/usr/bin/python3
""" class Square 
"""


class Square:
    """class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size 
        """
        return self.__siz

    @size.setter
    def size(self, value):
        """size"""
        if isinstance(value, int):
