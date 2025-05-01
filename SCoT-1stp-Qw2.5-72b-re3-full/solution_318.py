def max_volume(s):
    max_volume = 0
    for i in range(1, s - 1):
        for j in range(1, s - i):
            k = s - i - j
            volume = i * j * k
            if volume > max_volume:
                max_volume = volume
    return max_volume