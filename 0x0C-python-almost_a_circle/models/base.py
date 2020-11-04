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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json string to a file """""

        dict_list = []
        j_file = '{}.json'.format(cls.__name__)

        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

        j_string = Base.to_json_string(dict_list)
        with open(j_file, mode='w', encoding='utf-8') as a_file:
            a_file.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """Returning a list from a json string representation"""""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
