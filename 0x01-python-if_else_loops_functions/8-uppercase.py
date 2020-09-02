#!/usr/bin/python3
def uppercase(str):
    for l in range(len(str)):
        letter = ord(str[l])
        if (letter >= 97 and letter <= 122):
           letter -= 32
        print("{}".format(chr(letter)), end="")
    print()
