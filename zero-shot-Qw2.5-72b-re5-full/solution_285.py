import re

def text_match_two_three(text):
    """
    Write a function that matches a string that has an a followed by two to three 'b'.
    """
    pattern = r'ab{2,3}'
    return bool(re.search(pattern, text))