#!/usr/bin/python3
"""
Square class
"""


class Square:
    """__size (int): the size of the square
    """
    def __init__(self, size=0):
        """init
        """
        self.size = size

    @property
    def size(self):
        """size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area
        """
        return self.__size**2

    def my_print(self):
        """square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print('#'*self.__size)