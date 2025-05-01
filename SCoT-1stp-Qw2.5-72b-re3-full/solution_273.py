def substract_elements(test_tup1, test_tup2):
    # Initialize an empty list to store the results
    result_list = []
    
    # Iterate over the indices of the tuples
    for i in range(len(test_tup1)):
        # Subtract the element in test_tup2 from the element in test_tup1
        result = test_tup1[i] - test_tup2[i]
        # Append the result to the results list
        result_list.append(result)
    
    # Convert the results list to a tuple
    result_tup = tuple(result_list)
    
    # Return the result tuple
    return result_tup