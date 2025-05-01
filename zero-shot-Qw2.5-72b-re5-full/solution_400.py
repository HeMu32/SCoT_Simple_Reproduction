from collections import Counter

def extract_freq(test_list):
    sorted_tuples = [tuple(sorted(t)) for t in test_list]
    return dict(Counter(sorted_tuples))