import re

def check_integer(text):
    # Define the regex pattern for an integer
    pattern = r'^[+-]?[0-9]+$'
    # Use regex to check if the string matches the pattern
    if re.match(pattern, text):
        return True
    else:
        return False