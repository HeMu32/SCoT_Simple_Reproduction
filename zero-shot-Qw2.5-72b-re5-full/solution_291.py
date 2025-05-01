def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same, diff = 0, k
    for _ in range(2, n + 1):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff