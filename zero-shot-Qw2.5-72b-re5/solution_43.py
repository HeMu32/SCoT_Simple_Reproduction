import re

def text_match(text):
    """
    Write a function to find sequences of lowercase letters joined with an underscore using regex.
    """
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, text)
    return matches