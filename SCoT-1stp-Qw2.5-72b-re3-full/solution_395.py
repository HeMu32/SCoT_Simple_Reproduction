def first_non_repeating_character(str1):
    char_count = {}
    
    # Count the occurrences of each character
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for char in str1:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character is found
    return None