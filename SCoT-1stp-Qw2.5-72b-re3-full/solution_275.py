def get_Position(a, n, m):
    pos = m
    count = len(a)
    
    while count > 1:
        pos = (pos + n - 1) % count
        a.pop(pos)
        count -= 1
    
    # The last remaining element's position in the original list
    return pos

# Example usage:
a = [1, 2, 3, 4, 5]
n = 2
m = 0
print(get_Position(a, n, m))  # Output: 2