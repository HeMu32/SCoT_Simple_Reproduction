def common_in_nested_lists(nestedlist):
    # Initialize the set with the first sublist's elements
    common_elements = set(nestedlist[0])
    
    # Loop through the rest of the sublists
    for sublist in nestedlist[1:]:
        # Update the set to keep only elements that are in the current sublist
        common_elements.intersection_update(sublist)
    
    # Convert the set to a list and return it
    return list(common_elements)