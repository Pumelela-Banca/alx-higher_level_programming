#!/usr/bin/python3

"""
function adds lines after certain characters
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: '.', '?' and ':'
    :param text: text to indent
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        print()
        return

    new = ''
    for x in range(0, len(text)):
        if text[x] in ".?:":
            new += text[x]
            print(remove_white(new))
            new = ""
        else:
            new += text[x]
