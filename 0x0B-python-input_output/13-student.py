#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        """tnit"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """reload from json
        """
        for k, v in json.items():
            self.__dict__[k] = v