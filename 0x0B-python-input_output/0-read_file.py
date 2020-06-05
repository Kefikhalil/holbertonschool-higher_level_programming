#!/usr/bin/python3
'''Read file'''


def read_file(filename=""):
   '''Read file'''

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
