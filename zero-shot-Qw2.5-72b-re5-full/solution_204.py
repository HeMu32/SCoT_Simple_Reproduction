def count(s, c):
    res = 0
    for i in range(len(s)):
        if (s[i] == c):
            res += 1
    return res