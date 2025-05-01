def remove_tuples(test_list, K):
    result = []
    for item in test_list:
        if not (isinstance(item, tuple) and len(item) == K):
            result.append(item)
    return result