from collections import Counter

def check_occurences(test_list):
    flattened_list = [item for sublist in test_list for item in sublist]
    occurrences = Counter(flattened_list)
    return occurrences