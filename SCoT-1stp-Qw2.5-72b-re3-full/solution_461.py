def upper_ctr(str):
    count = 0
    for char in str:
        if char.isupper():
            count += 1
    return count