def find_tuples(test_list, K):
    result = []
    for tup in test_list:
        if all(x % K == 0 for x in tup):
            result.append(tup)
    return result