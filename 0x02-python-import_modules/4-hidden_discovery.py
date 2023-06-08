#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    all = dir(hidden_4)
    for x in all:
        if x[0:3] == "__":
            continue
        else:
            print(x)
