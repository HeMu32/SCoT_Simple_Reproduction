def sequence(n):
    if n == 1 or n == 2:
        return 1
    seq = [1, 1]
    for i in range(3, n + 1):
        next_val = seq[seq[i - 2] - 1] + seq[i - seq[i - 2] - 1]
        seq.append(next_val)
    return seq[n - 1]