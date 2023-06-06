#!/usr/bin/python3
x = 97
while x < 123:
    if x == 101 or x == 113:
        x += 1
        continue
    print("{:c}".format(x), end='')
    x += 1
