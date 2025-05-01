def number_of_substrings(str):
    n = len(str)
    count = n * (n + 1) // 2
    return count