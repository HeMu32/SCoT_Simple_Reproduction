import re

def check_literals(text, patterns):
    # Initialize an empty list to store the matches
    matches = []
    
    # Loop through each pattern in the patterns list
    for pattern in patterns:
        # Find all occurrences of the pattern in the text
        for match in re.finditer(pattern, text):
            # Extract the start and end positions of the match
            start, end = match.span()
            # Append a tuple containing the pattern and the start and end positions to the matches list
            matches.append((pattern, start, end))
    
    # Return the matches list
    return matches