def re_order(A):
    non_zero = []
    zeroes = []
    for element in A:
        if element != 0:
            non_zero.append(element)
        else:
            zeroes.append(element)
    return non_zero + zeroes