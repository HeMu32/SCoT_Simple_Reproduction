def freq_count(list1):
    # Initialize an empty dictionary to store the frequency of each element
    frequency = {}
    
    # Loop through each element in the list
    for element in list1:
        # If the element is already a key in the dictionary, increment its count
        if element in frequency:
            frequency[element] += 1
        # Otherwise, add the element to the dictionary with a count of 1
        else:
            frequency[element] = 1
    
    # Return the dictionary containing the frequency of each element
    return frequency