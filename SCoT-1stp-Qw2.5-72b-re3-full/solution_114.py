def assign_freq(test_list):
    # Initialize a dictionary to store the frequency of each tuple
    freq_dict = {}
    
    # Loop through each tuple in the input list
    for tup in test_list:
        if tup in freq_dict:
            # Increment the frequency count if the tuple is already in the dictionary
            freq_dict[tup] += 1
        else:
            # Add the tuple to the dictionary with a frequency of 1
            freq_dict[tup] = 1
    
    # Initialize a list to store the result
    result = []
    
    # Loop through each tuple in the input list
    for tup in test_list:
        # Append a new tuple to the result list, consisting of the original tuple and its frequency
        result.append((tup, freq_dict[tup]))
    
    # Return the result list
    return result