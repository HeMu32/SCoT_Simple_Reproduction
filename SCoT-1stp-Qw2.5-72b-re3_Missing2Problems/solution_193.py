def remove_tuple(test_tup):
    # Convert the tuple to a set to remove duplicates
    unique_set = set(test_tup)
    # Convert the set back to a tuple
    res = tuple(unique_set)
    return res