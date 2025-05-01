from collections import Counter

def extract_freq(test_list):
    freq_dict = Counter()
    for t in test_list:
        # Sort the tuple to treat (1, 2) and (2, 1) as the same
        sorted_t = tuple(sorted(t))
        # Update the frequency of the sorted tuple
        freq_dict[sorted_t] += 1
    return dict(freq_dict)