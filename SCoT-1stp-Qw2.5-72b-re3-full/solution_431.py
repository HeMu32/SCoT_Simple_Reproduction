def common_element(list1, list2):
    # Convert list1 to a set for efficient look-up
    set1 = set(list1)
    
    # Iterate through each element in list2
    for element in list2:
        # Check if the element exists in set1
        if element in set1:
            # If a common element is found, return True
            return True
    
    # If no common elements are found, return False
    return False