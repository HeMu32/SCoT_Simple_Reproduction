import re

def is_allowed_specific_char(string):
    # Define the pattern for allowed characters
    pattern = r'^[a-zA-Z0-9]+$'
    
    # Check if the string matches the pattern
    if re.fullmatch(pattern, string):
        return True
    else:
        return False