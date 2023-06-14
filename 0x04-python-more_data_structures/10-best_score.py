

def best_score(a_dictionary):
    """
    returns key with biggest value
    @a_dictionary: data
    Return: key
    """
    if a_dictionary is None:
        return None
    elif len(list(a_dictionary.keys())) == 1:
        return list(a_dictionary.keys())[0]
    else:
        start = a_dictionary[list(a_dictionary.keys())[0]]
        key = ''
        for x in list(a_dictionary.keys()):
            if  a_dictionary[x] >= start:
                start = a_dictionary[x]
                key = x
    return key
