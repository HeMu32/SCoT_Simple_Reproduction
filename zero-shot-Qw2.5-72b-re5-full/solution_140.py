def extract_singly(test_list):
    from collections import Counter
    count = Counter(test_list)
    return [item for item, cnt in count.items() if cnt == 1]