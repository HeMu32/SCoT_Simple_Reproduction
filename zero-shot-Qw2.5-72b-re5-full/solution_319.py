import re

def find_long_word(text): 
    """
    Write a function to find all five characters long word in the given string by using regex. 
    """ 
    pattern = r'\b\w{5}\b'
    return re.findall(pattern, text)