#!/usr/bin/python3
""" Creates object from json
file"""
import json


def load_from_json_file(filename):
    """ creates an Object fron a json
    file"""
    with open(filename, mode="r") as my_file:
        return json.load(my_file)
