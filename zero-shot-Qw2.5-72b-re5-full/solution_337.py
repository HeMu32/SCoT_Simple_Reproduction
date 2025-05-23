import re

def text_match_word(text):
    """
    Write a function that matches a word at the end of a string, with optional punctuation.
    """
    pattern = r'\b\w+\b[.,!?]*$'
    match = re.search(pattern, text)
    return match.group(0) if match else None