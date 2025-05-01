def minimum_Length(s):
    """
    Write a python function to minimize the length of the string by removing occurrence of only one character.
    """
    if not s:
        return 0
    
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    min_length = len(s)
    for count in char_count.values():
        min_length = min(min_length, len(s) - count)
    
    return min_length