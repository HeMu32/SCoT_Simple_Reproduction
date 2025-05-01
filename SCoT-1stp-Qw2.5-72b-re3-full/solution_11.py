def remove_Occ(s, ch):
    first_index = -1
    last_index = -1
    
    for i in range(len(s)):
        if s[i] == ch:
            if first_index == -1:
                first_index = i
            last_index = i
    
    if first_index == -1 and last_index == -1:
        return s  # No occurrences of ch found
    
    if first_index == last_index:
        return s[:first_index] + s[first_index + 1:]  # Only one occurrence found
    
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]  # Both first and last occurrences found