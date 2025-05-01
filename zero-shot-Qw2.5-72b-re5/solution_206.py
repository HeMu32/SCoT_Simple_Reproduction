def concatenate_elements(test_tup):
    return tuple(str(a) + str(b) for a, b in zip(test_tup, test_tup[1:]))