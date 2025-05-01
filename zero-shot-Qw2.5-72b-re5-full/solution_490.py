def extract_symmetric(test_list):
    """
    Write a function to extract all the pairs which are symmetric in the given tuple list.
    """
    symmetric_pairs = [pair for pair in test_list if (pair[1], pair[0]) in test_list]
    return symmetric_pairs