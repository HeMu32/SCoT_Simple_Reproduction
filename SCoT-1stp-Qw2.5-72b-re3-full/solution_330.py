import re

def find_char(text):
    # Define the regex pattern to match words of 3, 4, or 5 characters
    pattern = r'\b\w{3,5}\b'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Return the list of matched words
    return matches