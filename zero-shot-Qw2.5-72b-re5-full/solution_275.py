def get_Position(a, n, m):
    position = -1
    while n > 0:
        position = (position + m) % n
        n -= 1
    return position