def odd_bit_set_number(n):
    mask = 0
    bit_position = 1
    while bit_position <= n.bit_length():
        if bit_position % 2 != 0:
            mask |= (1 << (bit_position - 1))
        bit_position += 1
    return n | mask