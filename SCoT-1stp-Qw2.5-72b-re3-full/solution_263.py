def merge_dict(d1, d2):
    # Initialize an empty dictionary to store the merged result
    merged_dict = {}
    
    # Add all key-value pairs from d1 to merged_dict
    for key, value in d1.items():
        merged_dict[key] = value
    
    # Add all key-value pairs from d2 to merged_dict, overwriting any existing keys
    for key, value in d2.items():
        merged_dict[key] = value
    
    # Return the merged dictionary
    return merged_dict