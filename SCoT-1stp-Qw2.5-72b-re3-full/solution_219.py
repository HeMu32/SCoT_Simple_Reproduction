def extract_min_max(test_tup, K):
    # Convert the tuple to a list
    test_list = list(test_tup)
    
    # Sort the list in ascending order
    test_list.sort()
    
    # Extract the first K elements (smallest)
    min_elements = test_list[:K]
    
    # Extract the last K elements (largest)
    max_elements = test_list[-K:]
    
    # Combine the two lists
    result_list = min_elements + max_elements
    
    # Convert the result list back to a tuple
    result_tuple = tuple(result_list)
    
    # Return the resulting tuple
    return result_tuple