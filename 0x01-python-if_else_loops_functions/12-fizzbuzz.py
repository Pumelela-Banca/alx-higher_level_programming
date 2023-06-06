#!/usr/bin/python3

def fizzbuzz():
    """
    fizzbuzz - prints from 0 to 100 replacing 5x, 3x

    Return: void
    """
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz", end='')
        elif x % 5 == 0:
            print("Buzz", end='')
        elif x % 3 == 0:
            print("Fizz", end='')
        else:
            print(x, end='')
        print(" ", end='')
