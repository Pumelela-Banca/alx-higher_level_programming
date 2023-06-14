

def update_dictionary(a_dictionary, key, value):
    """
    update a dictionary
    @a_dictionary: data
    @key: update
    @value: new data
    """
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary.update({key: value})
    return a_dictionary
