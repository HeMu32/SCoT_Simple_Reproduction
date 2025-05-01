def replace_list(list1, list2):
    # Check if list1 is not empty
    if list1:
        # Remove the last element from list1
        list1.pop()
        # Append list2 to the end of list1
        list1.extend(list2)
    else:
        # If list1 is empty, return list2
        return list2
    # Return the modified list1
    return list1