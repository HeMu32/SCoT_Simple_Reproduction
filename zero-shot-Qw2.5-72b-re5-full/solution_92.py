def is_undulating(n):
    n_str = str(n)
    if len(n_str) < 3:
        return False
    for i in range(2, len(n_str)):
        if n_str[i] != n_str[i % 2]:
            return False
    return True