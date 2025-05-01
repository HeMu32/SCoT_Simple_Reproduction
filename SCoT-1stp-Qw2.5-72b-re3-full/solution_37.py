def sort_mixed_list(mixed_list):
    # Separate integers and strings
    integers = [x for x in mixed_list if isinstance(x, int)]
    strings = [x for x in mixed_list if isinstance(x, str)]
    
    # Sort the integers and strings separately
    integers.sort()
    strings.sort()
    
    # Concatenate the sorted lists
    sorted_list = integers + strings
    
    return sorted_list