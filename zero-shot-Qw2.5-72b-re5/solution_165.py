def count_char_position(str1):
    count = 0
    str1 = str1.lower()
    for i in range(len(str1)):
        if i == ord(str1[i]) - ord('a'):
            count += 1
    return count