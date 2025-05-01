import re

def find_long_word(text):
    # Define the regex pattern to match words that are exactly five characters long
    pattern = r'\b\w{5}\b'
    # Use re.findall to find all occurrences of the pattern in the text
    words = re.findall(pattern, text)
    # Return the list of matched words
    return words