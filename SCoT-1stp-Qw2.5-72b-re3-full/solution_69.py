def is_sublist(l, s):
    # If the sublist is longer than the list, it cannot be a sublist
    if len(s) > len(l):
        return False
    
    # Iterate over the list with an index
    for i in range(len(l) - len(s) + 1):
        # Check if the slice of l from i to i + len(s) matches s
        if l[i:i + len(s)] == s:
            return True
    
    # If no match is found, return False
    return False