import re

def remove_whitespaces(text1):
    # Use re.sub to replace all whitespace characters with an empty string
    return re.sub(r'\s+', '', text1)