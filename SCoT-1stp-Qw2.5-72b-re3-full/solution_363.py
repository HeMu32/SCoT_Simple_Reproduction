def add_K_element(test_list, K):
    result = []
    for tup in test_list:
        new_tuple = [elem + K for elem in tup]
        result.append(tuple(new_tuple))
    return result