import re

def text_match_string(text):
    # Define a regex pattern that matches a word at the beginning of a string
    pattern = r'^\w+'
    
    # Use the regex pattern to search the input text
    match = re.search(pattern, text)
    
    # If the search returns a match, return True
    if match:
        return True
    # Else, return False
    else:
        return False