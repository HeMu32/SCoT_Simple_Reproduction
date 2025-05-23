from collections import Counter

def rearrange_string(S):
    cnt = Counter(S)
    max_count = max(cnt.values())
    most_common_char = cnt.most_common(1)[0][0]
    
    if max_count > (len(S) + 1) // 2:
        return ""
    
    result = [''] * len(S)
    index = 0
    
    # Place the most common character first
    for char in most_common_char:
        for _ in range(cnt[char]):
            if index >= len(S):
                index = 1  # Start from the second position
            result[index] = char
            index += 2
    
    # Place the rest of the characters
    for char, count in cnt.items():
        if char == most_common_char:
            continue
        for _ in range(count):
            if index >= len(S):
                index = 1  # Start from the second position
            result[index] = char
            index += 2
    
    return ''.join(result)