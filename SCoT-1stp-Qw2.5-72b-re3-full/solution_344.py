def count_Odd_Squares(n, m):
    count = 0
    for i in range(n, m + 1):
        factor_count = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if i // j == j:
                    factor_count += 1
                else:
                    factor_count += 2
        if factor_count % 2 == 1:
            count += 1
    return count