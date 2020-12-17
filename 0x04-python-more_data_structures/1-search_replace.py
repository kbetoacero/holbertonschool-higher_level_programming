#!/usr/bin/python3
def search_replace(my_list, search, replace):
    find = [n if n != search else replace for n in my_list]
    return find
