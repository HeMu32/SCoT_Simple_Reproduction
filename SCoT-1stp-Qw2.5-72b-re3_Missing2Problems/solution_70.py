def get_equal(Input, k):
    if not Input:  # Check if the list is empty
        return True  # An empty list is considered to have tuples of equal length
    
    first_length = len(Input[0])  # Get the length of the first tuple
    all_equal = True  # Assume all tuples are of equal length
    
    for tup in Input:
        if len(tup) != first_length:
            all_equal = False
            break
    
    return all_equal