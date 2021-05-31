#!/usr/bin/python3
""" writes an object to a text
file"""

import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text
    file using a JSON representation
    """
    with open(filename, mode="w") as my_file:
        my_file.write(json.dumps(my_obj))
