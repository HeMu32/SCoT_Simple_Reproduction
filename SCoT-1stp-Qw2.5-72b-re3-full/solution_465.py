def drop_empty(dict1):
    # Initialize a new dictionary to store non-empty items
    new_dict = {}
    
    # Loop through each key-value pair in the input dictionary
    for key, value in dict1.items():
        # Check if the value is not empty
        if value:
            # Add the key-value pair to the new dictionary
            new_dict[key] = value
    
    # Return the new dictionary with non-empty items
    return new_dict