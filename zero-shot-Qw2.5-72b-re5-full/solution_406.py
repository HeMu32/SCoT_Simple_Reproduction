def find_Parity(x):
    parity = 0
    while x:
        parity = ~parity
        x = x & (x - 1)
    return parity & 1