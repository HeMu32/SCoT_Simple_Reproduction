def get_max_occuring_char(str1):
    # Initialize a dictionary to store the frequency of each character
    char_frequency = {}
    
    # Loop through each character in the string
    for char in str1:
        # If the character is not in the dictionary, add it with a count of 1
        if char not in char_frequency:
            char_frequency[char] = 1
        # If the character is already in the dictionary, increment its count by 1
        else:
            char_frequency[char] += 1
    
    # Initialize variables to track the character with the maximum frequency
    max_char = None
    max_count = 0
    
    # Loop through the dictionary to find the character with the maximum frequency
    for char, count in char_frequency.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    # Return the character with the maximum frequency
    return max_char