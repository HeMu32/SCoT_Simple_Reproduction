def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    elif n == -1:
        return -1
    else:
        return n | (n + 1)