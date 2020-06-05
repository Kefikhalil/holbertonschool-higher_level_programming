#!/usr/bin/python3
'''Read file'''


def read_file(filename=""):
   '''Read file'''

    with open(filename, 'r', encoding='UTF8') as file:
        print(file.read(), end="")
