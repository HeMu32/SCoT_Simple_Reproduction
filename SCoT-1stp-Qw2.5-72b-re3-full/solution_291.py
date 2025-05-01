def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k * k
    
    same = k  # The number of ways to paint the fence with the last two posts the same color
    diff = k * (k - 1)  # The number of ways to paint the fence with the last two posts different colors
    
    for _ in range(3, n + 1):
        new_diff = (same + diff) * (k - 1)
        same = diff
        diff = new_diff
    
    return same + diff