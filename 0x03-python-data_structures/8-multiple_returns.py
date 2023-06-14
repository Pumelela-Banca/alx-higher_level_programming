#!/usr/bin/python3

def multiple_returns(sentence):
    """
    multiple_returns - returns lenght of  string and first character
    @sentence: string
    """
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
