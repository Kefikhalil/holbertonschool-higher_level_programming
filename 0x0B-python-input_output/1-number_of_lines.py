#!/usr/bin/python3
''' Number of lines '''


def number_of_lines(filename=""):
    ''' Number of lines '''
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)
