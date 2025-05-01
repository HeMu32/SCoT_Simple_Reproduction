def cal_sum(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    
    p0, p1, p2 = 3, 0, 2
    total = p0 + p1 + p2
    
    for _ in range(3, n + 1):
        p_next = p0 + p1
        total += p_next
        p0, p1, p2 = p1, p2, p_next
    
    return total