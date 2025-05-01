import re

def multiple_split(text):
    # Define the delimiters
    delimiters = ' ,;.'  # Example delimiters: space, comma, semicolon, and period
    # Create a regex pattern to match any of the delimiters
    pattern = '[' + re.escape(delimiters) + ']'
    # Split the text using the regex pattern
    result = re.split(pattern, text)
    # Filter out any empty strings that may result from consecutive delimiters
    result = [s for s in result if s]
    return result