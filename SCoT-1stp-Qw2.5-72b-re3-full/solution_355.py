import math

def count_Rectangles(radius):
    count = 0
    for w in range(1, radius + 1):
        for h in range(1, radius + 1):
            diagonal = math.sqrt(w**2 + h**2)
            if diagonal <= radius:
                count += 1
    return count