def check_distinct(test_tup):
    # Convert the tuple to a set to remove duplicates
    test_set = set(test_tup)
    # Compare the lengths of the tuple and the set
    if len(test_tup) == len(test_set):
        # If lengths are equal, all elements are distinct
        return True
    else:
        # If lengths are not equal, there are duplicates
        return False