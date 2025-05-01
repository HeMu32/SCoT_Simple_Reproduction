import re

def check_literals(text, patterns):
    """
    Write a function to search some literals strings in a string by using regex.
    """
    results = {}
    for pattern in patterns:
        matches = re.findall(pattern, text)
        results[pattern] = matches
    return results