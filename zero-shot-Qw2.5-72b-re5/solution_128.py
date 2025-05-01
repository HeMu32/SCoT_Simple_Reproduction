def long_words(n, str):
    """
    Write a function to shortlist words that are longer than n from a given list of words.
    """
    words = str.split()
    long_words_list = [word for word in words if len(word) > n]
    return long_words_list