def Find_Min(lst):
    # Initialize min_length with infinity and min_sublist as None
    min_length = float('inf')
    min_sublist = None
    
    # Iterate through each sublist in the input list
    for sublist in lst:
        # Check if the current sublist's length is less than the current minimum length
        if len(sublist) < min_length:
            # Update min_length and min_sublist
            min_length = len(sublist)
            min_sublist = sublist
    
    # Return the sublist with the minimum length
    return min_sublist