#!/usr/bin/python3
""" Studen to JSON """


class Student:
    """ Studen Class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        a = self.__dict__
        return a
