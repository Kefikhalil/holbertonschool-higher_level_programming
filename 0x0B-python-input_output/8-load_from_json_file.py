#!/usr/bin/python3
"""Create object from a JSON file"""


def load_from_json_file(filename):
    '''Create object from a JSON file'''

    import json
    with open(filename, encoding='UTF8') as file:
        return json.load(file)
