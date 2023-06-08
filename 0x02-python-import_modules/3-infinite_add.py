#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    sum_all = 0
    for x in argv:
        sum_all += int(x)
    print(sum_all)
