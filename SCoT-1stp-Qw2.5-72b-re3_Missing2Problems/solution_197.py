def find_exponentio(test_tup1, test_tup2):
    # Ensure both tuples have the same length
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Both tuples must have the same length")
    
    # Initialize an empty list to store the results
    result_list = []
    
    # Loop through each index of the tuples
    for i in range(len(test_tup1)):
        # Compute the exponentiation
        result = test_tup1[i] ** test_tup2[i]
        # Append the result to the list
        result_list.append(result)
    
    # Convert the list to a tuple and return it
    result_tup = tuple(result_list)
    return result_tup