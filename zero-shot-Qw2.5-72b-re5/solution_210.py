import re

def is_allowed_specific_char(string):
    """
    Write a function to check that the given string contains only a certain set of characters(in this case a-z, A-Z and 0-9) by using regex.
    """
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    return bool(pattern.match(string))