import re

def is_valid_URL(url):
    # Define the regex pattern for a valid URL
    pattern = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[^ \n]*)?$'
    
    # Use re.match to check if the URL matches the pattern
    if re.match(pattern, url):
        return True
    else:
        return False