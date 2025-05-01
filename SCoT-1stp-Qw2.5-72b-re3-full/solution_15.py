import re

def split_lowerstring(text):
    # Split the string at each lowercase letter
    parts = re.split('([a-z])', text)
    # Filter out any empty strings that may result from the split
    parts = [part for part in parts if part]
    return parts