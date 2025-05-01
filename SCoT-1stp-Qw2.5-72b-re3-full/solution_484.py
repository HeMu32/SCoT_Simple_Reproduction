def remove_matching_tuple(test_list1, test_list2):
    result = []
    for t1 in test_list1:
        if t1 not in test_list2:
            result.append(t1)
    for t2 in test_list2:
        if t2 not in test_list1:
            result.append(t2)
    return result