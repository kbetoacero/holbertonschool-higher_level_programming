#!/usr/bin/python3
""" Student to JSON"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for item in attrs:
                if hasattr(self, item):
                    new_dict[item] = getattr(self, item)
        return (new_dict)

    def reload_from_json(self, json):
        """ Function that replaces all atrribs
        of a student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
