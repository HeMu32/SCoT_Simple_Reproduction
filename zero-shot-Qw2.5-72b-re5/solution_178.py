def string_literals(patterns, text):
    """
    Write a function to search some literals strings in a string.
    """
    found = {}
    for pattern in patterns:
        if pattern in text:
            found[pattern] = True
        else:
            found[pattern] = False
    return found