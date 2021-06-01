#!/usr/bin/python3
""" load, add, save"""

import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    filename = load_from_json_file("add_item.json")
except:
    filename = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        filename.append(sys.argv[i])
save_to_json_file(filename, "add_item.json")
