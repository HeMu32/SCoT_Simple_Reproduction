def Find_Min_Length(lst):
    if not lst:  # Check if the list is empty
        return 0  # Return 0 if the list is empty, as there are no sublists to measure
    min_length = len(lst[0])  # Initialize min_length with the length of the first sublist
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)
    return min_length