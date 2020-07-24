#!/usr/bin/python3
'''class suqare'''


class Square:
    '''Square class
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''init
        '''

        self.size = size
        self.position = position

    @property
    def size(self):
        '''size
        '''

        return self.__size

    @size.setter
    def size(self, value):
        '''size
        '''

        if not type(value) is int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        '''position
        '''
        return self.__position

    @position.setter
    def position(self, position):
        '''position
        '''

        if type(position) != tuple or len(position) != 2\
                or type(position[0]) != int\
                or type(position[1]) != int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        '''area
        '''
        return self.__size ** 2

    def my_print(self):
        '''my print
        '''

        if self.__size == 0:
            print()

        else:
            print("\n" * self.__position[1], end='')
            for i in range(0, self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)