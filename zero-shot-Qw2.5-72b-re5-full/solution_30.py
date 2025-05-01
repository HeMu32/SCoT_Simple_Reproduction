def check_Equality(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                count += 1
    return count