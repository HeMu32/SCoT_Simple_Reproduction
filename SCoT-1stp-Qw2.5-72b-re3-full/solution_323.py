def re_arrange(arr, n):
    pos = []
    neg = []
    
    # Separate positive and negative numbers
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    
    result = []
    i, j = 0, 0
    
    # Alternate between positive and negative numbers
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
    
    # Append any remaining positive numbers
    while i < len(pos):
        result.append(pos[i])
        i += 1
    
    # Append any remaining negative numbers
    while j < len(neg):
        result.append(neg[j])
        j += 1
    
    return result