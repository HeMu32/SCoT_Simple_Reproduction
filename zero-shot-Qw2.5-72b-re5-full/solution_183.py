def count_pairs(arr, n, k):
    from collections import Counter
    count = 0
    freq = Counter(arr)
    for num in freq:
        if num + k in freq:
            count += freq[num] * freq[num + k]
    return count