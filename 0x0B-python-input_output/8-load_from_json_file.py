#!/usr/bin/python3
""" Creates object form a JSON file
    """
import json


def load_from_json_file(filename):
    """ creates an Object from a
    JSON file """
    with open(filename, mode='r') as a_file:
        return json.load(a_file)
