def find_Element(arr, rotations, index):
    # Calculate the effective number of rotations
    effective_rotations = rotations % len(arr)
    
    # If no effective rotations, return the element at the given index
    if effective_rotations == 0:
        return arr[index]
    
    # Calculate the new index after the rotations
    new_index = (index + effective_rotations) % len(arr)
    
    # Return the element at the new index
    return arr[new_index]