import re

def snake_to_camel(word):
    # Use regex to find and replace all occurrences of '_[a-z]' with the uppercase of the letter
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), word)