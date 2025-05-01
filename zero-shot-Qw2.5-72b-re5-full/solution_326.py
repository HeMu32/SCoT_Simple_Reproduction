def most_occurrences(test_list):
    from collections import Counter
    if not test_list:
        return None
    word_counts = Counter(test_list)
    max_occurrence = max(word_counts.values())
    most_common_words = [word for word, count in word_counts.items() if count == max_occurrence]
    return most_common_words[0] if len(most_common_words) == 1 else most_common_words