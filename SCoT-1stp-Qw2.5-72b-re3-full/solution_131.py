def reverse_vowels(str1):
    vowels = 'aeiouAEIOU'
    found_vowels = []
    for ch in str1:
        if ch in vowels:
            found_vowels.append(ch)
    
    result = []
    vowel_index = len(found_vowels) - 1
    for ch in str1:
        if ch in vowels:
            result.append(found_vowels[vowel_index])
            vowel_index -= 1
        else:
            result.append(ch)
    
    return ''.join(result)