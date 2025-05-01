def count_Substrings(s, n):
    def is_valid(sub):
        return sum(int(char) for char in sub) == len(sub)
    
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if is_valid(s[i:j]):
                count += 1
    return count