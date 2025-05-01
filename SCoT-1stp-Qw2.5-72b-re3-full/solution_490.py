def extract_symmetric(test_list):
    symmetric_pairs = []
    seen = set()
    for pair in test_list:
        reverse_pair = (pair[1], pair[0])
        if reverse_pair in seen:
            symmetric_pairs.append(pair)
        seen.add(pair)
    return symmetric_pairs