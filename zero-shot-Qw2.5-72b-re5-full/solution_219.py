def extract_min_max(test_tup, K):
    sorted_tup = sorted(test_tup)
    min_k = sorted_tup[:K]
    max_k = sorted_tup[-K:]
    return min_k, max_k