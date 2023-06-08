#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    sum_all = 0
    if len(argv) == 1:
        print(0)
    elif len(argv) == 2:
        print(argv[1])
    else:
        for x in argv[1:]:
            sum_all += int(x)
        print(sum_all)
