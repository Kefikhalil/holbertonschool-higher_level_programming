#!/usr/bin/python3
import json
"""Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """Save Object to a file"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
    f.closed
