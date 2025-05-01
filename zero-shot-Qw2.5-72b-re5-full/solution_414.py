def overlapping(list1, list2):
    """
    Write a python function to check whether any value from list1 exists in list2 or not.
    """
    return any(item in list2 for item in list1)