def add_pairwise(test_tup):
    # Initialize an empty list to store the results of the pairwise additions
    res = []
    
    # Loop through the indices of the tuple, except the last one
    for i in range(len(test_tup) - 1):
        # Add the current element to the next element in the tuple
        sum_val = test_tup[i] + test_tup[i + 1]
        # Append the result of the addition to the results list
        res.append(sum_val)
    
    # Convert the results list into a tuple
    res = tuple(res)
    
    # Return the resulting tuple
    return res