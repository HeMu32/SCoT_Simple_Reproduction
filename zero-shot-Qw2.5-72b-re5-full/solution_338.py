def check_Equality(s):
    def is_same_first_last(sub):
        return sub[0] == sub[-1]

    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if is_same_first_last(s[i:j+1]):
                count += 1
    return count