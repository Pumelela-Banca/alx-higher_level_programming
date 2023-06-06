#!/usr/bin/python3

for i in range(0, 9):
    for y in range(i+1, 10):
        print("{}{}".format(i, y), end='')
        if (i + y) == 17:
            break
        else:
            print(", ", end='')
print()
