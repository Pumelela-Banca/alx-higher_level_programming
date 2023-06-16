

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
    for x in range(0, len(roman_string)):
        if x != (len(roman_string) -
                 1) and names[roman_string[x]
                              ] < names[roman_string[x + 1]]:
            sum_all += -1 * names[roman_string[x]]
        elif x != (len(roman_string) -
                   1) and (x == "I" and roman_string[
                       x + 1] == "V"):
            sum_all += 4
            break
        elif x != (len(roman_string) -
                   1) and (x == "I" and roman_string[
                       x + 1] == "X"):
            sum_all += 9
            break
        else:
            sum_all += names[roman_string[x]]
    return sum_all
