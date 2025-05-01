def even_bit_toggle_number(num):
    mask = 0
    bit_position = 0
    while (1 << bit_position) <= num:
        if bit_position % 2 == 1:
            mask |= (1 << bit_position)
        bit_position += 1
    return num ^ mask