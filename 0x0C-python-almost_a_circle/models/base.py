#!/usr/bin/python3
""" Base Class Module"""
import json
import csv


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Init Function """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ REturning json string representation
        from a list """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """ writes json string representation of
        list_objs to a file """


        if not list_objs:
            list_objs = []
        with open("{}.json".format(cls.__name__), 'w') as a_file:
            a_file.write(cls.to_json_string([obj.to_dictionary() for
                                             obj in list_objs]))
