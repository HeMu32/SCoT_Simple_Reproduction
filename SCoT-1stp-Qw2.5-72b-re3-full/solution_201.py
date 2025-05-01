def chkList(lst):
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return True
    
    # Get the first element of the list
    first_element = lst[0]
    
    # Loop through the list starting from the second element
    for element in lst[1:]:
        # If an element is not equal to the first element, return False
        if element != first_element:
            return False
    
    # If all elements are the same, return True
    return True