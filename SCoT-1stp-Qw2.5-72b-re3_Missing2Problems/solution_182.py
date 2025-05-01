import re

def find_character(string):
    # Initialize a dictionary to store the counts
    counts = {
        'uppercase': 0,
        'lowercase': 0,
        'special_characters': 0,
        'numeric_values': 0
    }
    
    # Regular expressions to find each category
    counts['uppercase'] = len(re.findall(r'[A-Z]', string))
    counts['lowercase'] = len(re.findall(r'[a-z]', string))
    counts['special_characters'] = len(re.findall(r'[^A-Za-z0-9]', string))
    counts['numeric_values'] = len(re.findall(r'[0-9]', string))
    
    return counts