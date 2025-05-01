import re

def check_char(string):
    """
    Write a function to check whether the given string starts and ends with the same character or not using regex.
    """
    pattern = r"^(.).*\1$"
    return bool(re.match(pattern, string))