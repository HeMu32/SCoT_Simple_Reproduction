import re

def remove_uppercase(str1):
    """ 
    Write a function to remove uppercase substrings from a given string by using regex. 
    """
    # Substitute all uppercase letters (A-Z) with an empty string
    result = re.sub(r'[A-Z]', '', str1)
    return result