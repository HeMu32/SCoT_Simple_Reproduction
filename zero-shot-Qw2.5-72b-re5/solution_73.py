import re

def multiple_split(text):
    """
    Write a function to split the given string with multiple delimiters by using regex.
    """
    delimiters = r'[ ,;.]'
    return re.split(delimiters, text)