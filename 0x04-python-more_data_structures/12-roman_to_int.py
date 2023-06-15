#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    roman_to_int - turns roman numbers to int
    @roman_string: roman string
    Return: integer
    """
    if len(roman_string) == 0 or roman_string is None:
        return 0

    if not isinstance(roman_string, str) or roman_string == '0':
        return 0

    names = {"I": 1, "II": 2, "III": 3, "IV": 4, "X": 10, "L": 50, "C": 100,
             "V": 5, "VI": 6, "VII": 7, "VIII": 8,
             "IX": 9, "D": 500, "M": 1000}

    sum_all = 0

    if roman_string in names.keys():
        return names[roman_string]

    for x in roman_string:
        if x not in names.keys():
            return 0
        sum_all += names[x]
    return sum_all
