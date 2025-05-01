def find_demlo(s):
    result = ''
    # Append numbers from 1 to s
    for i in range(1, s + 1):
        result += str(i)
    # Append numbers from s-1 down to 1
    for i in range(s - 1, 0, -1):
        result += str(i)
    return result