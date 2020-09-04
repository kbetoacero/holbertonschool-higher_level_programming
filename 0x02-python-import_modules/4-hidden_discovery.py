#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for namedef in dir(hidden_4):
        if namedef[:2] != "__":
            print(namedef)
