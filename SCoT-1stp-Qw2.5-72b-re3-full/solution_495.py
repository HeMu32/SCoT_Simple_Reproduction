import re

def remove_lowercase(str1):
    # Substitute all lowercase letters with an empty string
    result = re.sub('[a-z]', '', str1)
    return result