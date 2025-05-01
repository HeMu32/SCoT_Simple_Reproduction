def Find_Min_Length(lst):
    if not lst:  # Check if the list is empty
        return 0
    min_length = len(min(lst, key=len))
    return min_length