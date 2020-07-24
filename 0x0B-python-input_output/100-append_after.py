#!/usr/bin/python3
"""appending class
"""


def append_after(filename="", search_string="", new_string=""):
    """append_after
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        txt = ""
        for i in file:
            txt += i
            if search_string in i:
                txt += new_string
        file.seek(0)
        for i in txt:
            file.write(i)