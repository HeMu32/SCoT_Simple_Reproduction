def get_pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pell_0 = 0
        pell_1 = 1
        for _ in range(2, n + 1):
            pell_n = 2 * pell_1 + pell_0
            pell_0, pell_1 = pell_1, pell_n
        return pell_n