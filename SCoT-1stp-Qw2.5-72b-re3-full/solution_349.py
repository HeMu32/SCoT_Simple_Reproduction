def check(s):
    binary_chars = {'0', '1'}
    for c in s:
        if c not in binary_chars:
            return False
    return True