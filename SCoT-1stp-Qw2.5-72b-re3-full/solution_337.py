import re

def text_match_word(text):
    # Remove leading and trailing whitespace
    text = text.strip()
    
    # Split the text into words
    words = text.split()
    
    # Check if the text is empty or does not contain any words
    if not words:
        return False
    
    # Get the last word
    last_word = words[-1]
    
    # Remove trailing punctuation and store it
    punctuation = ''
    while last_word and not last_word[-1].isalnum():
        punctuation = last_word[-1] + punctuation
        last_word = last_word[:-1]
    
    # Check if the last word (after removing punctuation) is a word
    if last_word.isalpha():
        return True
    else:
        return False