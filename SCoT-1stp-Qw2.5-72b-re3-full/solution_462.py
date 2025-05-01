from itertools import combinations

def combinations_list(list1):
    result = []
    n = len(list1)
    for r in range(1, n + 1):
        for combo in combinations(list1, r):
            result.append(list(combo))
    return result