import re

def text_match_one(text):
    # Define the pattern
    pattern = 'ab+'
    
    # Search for the pattern in the text
    match = re.search(pattern, text)
    
    # Return True if the pattern is found, otherwise False
    return bool(match)