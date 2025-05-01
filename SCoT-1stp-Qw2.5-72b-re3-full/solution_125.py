def find_length(string, n):
    max_diff = 0
    count = 0
    for char in string:
        if char == '0':
            count += 1
        elif char == '1':
            count -= 1
        if count > max_diff:
            max_diff = count
        if count < 0:
            count = 0
    return max_diff