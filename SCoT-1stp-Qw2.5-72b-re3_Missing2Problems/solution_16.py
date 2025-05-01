import re

def text_lowercase_underscore(text):
    # Define the pattern to match sequences of lowercase letters joined with an underscore
    pattern = r'\b[a-z]+_[a-z]+\b'
    # Find all occurrences of the pattern
    matches = re.findall(pattern, text)
    # Return the list of matches
    return matches