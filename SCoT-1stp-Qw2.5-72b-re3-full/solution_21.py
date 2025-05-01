def multiples_of_num(m, n):
    multiples = []
    for i in range(1, m + 1):
        multiple = n * i
        multiples.append(multiple)
    return multiples