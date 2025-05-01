import math

def next_Perfect_Square(N):
    N += 1
    while True:
        root = math.sqrt(N)
        if root.is_integer():
            break
        N += 1
    return N