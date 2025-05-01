def neg_nos(list1):
    # Initialize an empty list to store negative numbers
    negative_numbers = []
    
    # Iterate over each element in the input list
    for num in list1:
        # Check if the current element is negative
        if num < 0:
            # Append the negative number to the list
            negative_numbers.append(num)
    
    # Return the list of negative numbers
    return negative_numbers