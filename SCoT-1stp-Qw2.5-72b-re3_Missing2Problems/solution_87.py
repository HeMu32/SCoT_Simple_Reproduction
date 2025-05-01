def merge_dictionaries_three(dict1, dict2, dict3):
    # Initialize an empty dictionary to store the merged results
    merged_dict = {}
    
    # Add all key-value pairs from dict1 to merged_dict
    for key, value in dict1.items():
        merged_dict[key] = value
    
    # Add all key-value pairs from dict2 to merged_dict
    for key, value in dict2.items():
        merged_dict[key] = value
    
    # Add all key-value pairs from dict3 to merged_dict
    for key, value in dict3.items():
        merged_dict[key] = value
    
    # Return the merged dictionary
    return merged_dict