def and_tuples(test_tup1, test_tup2):
    result_list = []
    for i in range(len(test_tup1)):
        if test_tup1[i] and test_tup2[i]:
            result_list.append(True)
        else:
            result_list.append(False)
    result_tup = tuple(result_list)
    return result_tup