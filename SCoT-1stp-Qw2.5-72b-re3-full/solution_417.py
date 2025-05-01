def group_tuples(Input):
    # Initialize an empty dictionary to store the grouped tuples
    grouped_dict = {}
    
    # Iterate over each tuple in the input list
    for tup in Input:
        # Extract the first element of the current tuple
        first_element = tup[0]
        
        # If the first element is not already a key in the dictionary
        if first_element not in grouped_dict:
            # Add the first element as a new key with an empty list as its value
            grouped_dict[first_element] = []
        
        # Append the current tuple to the list of the corresponding key
        grouped_dict[first_element].append(tup)
    
    # Return the dictionary
    return grouped_dict