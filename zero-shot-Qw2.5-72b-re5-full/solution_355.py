def count_Rectangles(radius):
    count = 0
    for width in range(1, radius * 2 + 1):
        for height in range(1, radius * 2 + 1):
            if (width // 2) ** 2 + (height // 2) ** 2 <= radius ** 2:
                count += 1
    return count