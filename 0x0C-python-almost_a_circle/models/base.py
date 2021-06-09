#!/usr/bin/python3
""" Base Class """


import json


class Base:

    """ Base Class
    public attribute __nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON reprsentation of list
        dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string representation
        of list_objs to a file"""
        file_name = "{}.json".format(cls.__name__)
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(cls.to_dictionary(obj))
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """  returns the list of the JSON string
        representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all
        attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        new_list = []
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, 'r') as file:
                new_list = cls.from_json_string(file.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new[i])
        except:
            pass
        return new_list
