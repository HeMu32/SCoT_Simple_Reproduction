def start_withp(words):
    result = []  # Initialize an empty list to store the words starting with 'p'
    for word in words:  # Loop through each word in the input list
        if word.lower().startswith('p'):  # Check if the word starts with 'p' (case-insensitive)
            result.append(word)  # Add the word to the result list
    return result  # Return the list of words starting with 'p'