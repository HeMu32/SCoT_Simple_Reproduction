def check_type(test_tuple):
    """
    Write a function to check if all the elements in tuple have same data type or not.
    """
    if not test_tuple:  # Check if the tuple is empty
        return True
    first_type = type(test_tuple[0])
    return all(type(element) == first_type for element in test_tuple)