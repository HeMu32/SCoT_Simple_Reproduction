def position_max(list1):
    # Find the maximum value in the list
    max_value = max(list1)
    
    # Initialize an empty list to store the indices of the maximum value
    positions = []
    
    # Loop through the list with index and value
    for index, value in enumerate(list1):
        # If the value is equal to the maximum value, append the index to the positions list
        if value == max_value:
            positions.append(index)
    
    # Return the positions list
    return positions