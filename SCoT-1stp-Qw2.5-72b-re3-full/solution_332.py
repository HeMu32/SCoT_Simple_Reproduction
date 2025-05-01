def char_frequency(str1):
    # Initialize an empty dictionary to store character frequencies
    freq_dict = {}
    
    # Loop through each character in the string
    for char in str1:
        # If the character is already in the dictionary, increment its count
        if char in freq_dict:
            freq_dict[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            freq_dict[char] = 1
    
    # Return the dictionary
    return freq_dict