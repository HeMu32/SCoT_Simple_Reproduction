def position_min(list1):
    positions = []
    if not list1:  # Check if the list is empty
        return positions
    min_value = min(list1)  # Find the minimum value in the list
    for index, value in enumerate(list1):  # Iterate over the list with index and value
        if value == min_value:  # Check if the current value is the minimum value
            positions.append(index)  # Append the index to the positions list
    return positions  # Return the list of positions