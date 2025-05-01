def char_frequency(str1):
    freq = {}
    for char in str1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq