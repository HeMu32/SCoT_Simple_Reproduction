def minimum_Length(s):
    min_length = len(s)
    for c in set(s):
        s_new = s.replace(c, '')
        if len(s_new) < min_length:
            min_length = len(s_new)
    return min_length