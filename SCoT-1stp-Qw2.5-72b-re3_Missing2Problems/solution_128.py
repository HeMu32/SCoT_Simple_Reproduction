def long_words(n, str):
    # Split the input string into a list of words
    words = str.split()
    
    # Initialize an empty list to store words longer than n characters
    long_words_list = []
    
    # Iterate over each word in the list
    for word in words:
        # Check if the length of the word is greater than n
        if len(word) > n:
            # Add the word to the list of long words
            long_words_list.append(word)
    
    # Return the list of long words
    return long_words_list