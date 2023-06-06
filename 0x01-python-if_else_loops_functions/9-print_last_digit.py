#!/usr/bin/python3

def print_last_digit(number):
    """
    print_last_digit - prints last digit of number
    number: number
    Return: values of last digit
    """

    if number == 0:
        num = 0
    elif number < 0:
        number = number * -1
        num = (number % 10)
    else:
        num = number % 10
    print(num, end='')
    return num
