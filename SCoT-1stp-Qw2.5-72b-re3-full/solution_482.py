import re

def match(text):
    # Define the regex pattern
    pattern = r'[A-Z][a-z]*'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Return the list of matches
    return matches