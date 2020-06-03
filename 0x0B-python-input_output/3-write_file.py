#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """Write to a file """

    with open(filename, 'w', encoding='utf8') as file:
        n = file.write(text)
    return(n)
