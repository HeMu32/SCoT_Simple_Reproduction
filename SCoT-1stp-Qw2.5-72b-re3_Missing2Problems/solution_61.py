def count_Substrings(s, n):
    count = 0
    for i in range(n):
        sum_of_digits = 0
        for j in range(i, n):
            if s[j].isdigit():
                sum_of_digits += int(s[j])
            if sum_of_digits == j - i + 1:
                count += 1
    return count