def check_Consecutive(l):
    if len(l) <= 1:
        return False
    l.sort()
    for i in range(len(l) - 1):
        if l[i] + 1 != l[i + 1]:
            return False
    return True