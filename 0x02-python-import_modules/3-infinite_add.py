#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    x = 0
    for arg in range(arguments):
        x += int(sys.argv[arg + 1])
    print("{}".format(x))
