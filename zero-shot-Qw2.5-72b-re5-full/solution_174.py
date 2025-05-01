def group_keyvalue(l):
    """
    Write a function to group a sequence of key-value pairs into a dictionary of lists.
    """
    result = {}
    for key, value in l:
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result