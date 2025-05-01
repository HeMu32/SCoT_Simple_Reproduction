def concatenate_strings(test_tup1, test_tup2):
    # Initialize an empty list to store the concatenated strings
    concatenated_list = []
    
    # Loop through each string in test_tup1 and test_tup2
    for str1, str2 in zip(test_tup1, test_tup2):
        # Concatenate the strings
        concatenated_str = str1 + str2
        # Append the concatenated string to the list
        concatenated_list.append(concatenated_str)
    
    # Convert the list of concatenated strings back to a tuple
    concatenated_tuple = tuple(concatenated_list)
    
    # Return the tuple of concatenated strings
    return concatenated_tuple