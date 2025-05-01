def find_Max_Len_Even(str):
    # Split the string into a list of words
    words = str.split()
    
    # Initialize max_len to -1
    max_len = -1
    
    # Loop through each word in the list
    for word in words:
        # Calculate the length of the current word
        word_len = len(word)
        
        # Check if the length is even and greater than max_len
        if word_len % 2 == 0 and word_len > max_len:
            max_len = word_len
            break  # We found the first maximum length even word, so we can stop
    
    # Return the maximum length of an even word or -1 if none found
    return max_len