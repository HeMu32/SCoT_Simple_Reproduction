def tuple_int_str(tuple_str):
    # Initialize an empty list to store the integer values
    int_list = []
    
    # Loop through each element in the input tuple
    for item in tuple_str:
        # Convert the current string element to an integer
        int_value = int(item)
        # Append the converted integer to the list
        int_list.append(int_value)
    
    # Convert the list of integers to a tuple
    tuple_int = tuple(int_list)
    # Return the tuple of integers
    return tuple_int