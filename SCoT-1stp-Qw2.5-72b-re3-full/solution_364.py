def min_flip_to_make_string_alternate(s):
    flip0 = 0  # Flips needed if the string starts with '0'
    flip1 = 0  # Flips needed if the string starts with '1'
    
    for i in range(len(s)):
        if i % 2 == 0:  # Even index
            if s[i] == '1':
                flip0 += 1
            else:
                flip1 += 1
        else:  # Odd index
            if s[i] == '0':
                flip0 += 1
            else:
                flip1 += 1
    
    return min(flip0, flip1)