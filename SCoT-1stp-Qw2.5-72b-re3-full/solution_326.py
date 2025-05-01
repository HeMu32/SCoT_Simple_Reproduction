def most_occurrences(test_list):
    word_count = {}
    for string in test_list:
        words = string.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    max_word = None
    max_count = 0
    for word, count in word_count.items():
        if count > max_count:
            max_word = word
            max_count = count
    
    return max_word