#!/usr/bin/python3
for letter in range (25, -1, -1):
    print("{:s}".format(chr(letter + ord('a')) if letter % 2 else chr(letter + ord('A'))),
        end="")
