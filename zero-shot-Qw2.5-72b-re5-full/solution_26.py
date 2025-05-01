def check_k_elements(test_list, K):
    """
    Write a function to check if the given tuple list has all k elements.
    """
    return all(len(tup) == K for tup in test_list)