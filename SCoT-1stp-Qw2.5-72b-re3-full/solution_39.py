def rearrange_string(S):
    from collections import Counter
    
    # Count the frequency of each character
    char_count = Counter(S)
    
    # Find the maximum frequency of any character
    max_freq = max(char_count.values())
    
    # Check if the maximum frequency is more than half the length of the string plus one
    if max_freq > (len(S) + 1) // 2:
        return False
    else:
        return True