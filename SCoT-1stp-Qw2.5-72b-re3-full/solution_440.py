import re

def find_adverb_position(text):
    # Initialize an empty list to store the adverbs and their positions
    adverbs = []
    
    # Split the text into words
    words = text.split()
    
    # Loop through each word in the text
    for i, word in enumerate(words):
        # Check if the word ends with "ly"
        if word.endswith('ly'):
            # Record the word and its position in the text
            start_position = text.find(word, sum(len(w) + 1 for w in words[:i]))
            adverbs.append((word, start_position))
    
    # Return the list of adverbs and their positions
    return adverbs