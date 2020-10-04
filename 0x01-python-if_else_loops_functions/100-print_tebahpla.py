#!/usr/bin/python3
for x in range(25, -1, -1):
    print("{:s}".format(chr(x + ord('a')) if x % 2 else chr(x + ord('A'))),
          end="")
