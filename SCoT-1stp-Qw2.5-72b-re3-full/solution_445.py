def index_multiplication(test_tup1, test_tup2):
    result_list = []
    if len(test_tup1) != len(test_tup2):
        return None
    for i in range(len(test_tup1)):
        result_list.append(test_tup1[i] * test_tup2[i])
    result_tup = tuple(result_list)
    return result_tup