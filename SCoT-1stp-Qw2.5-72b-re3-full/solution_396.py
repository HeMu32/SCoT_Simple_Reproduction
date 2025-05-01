import re

def check_char(string):
    # Define the regex pattern to match strings that start and end with the same character
    pattern = r'^(.).*\1$'
    
    # Use re.match to check if the string matches the pattern
    match = re.match(pattern, string)
    
    # Return True if a match is found, otherwise return False
    return bool(match)