def check(s):
    """
    Write a python function to check whether the given string is a binary string or not.
    """
    return all(c in '01' for c in s)