def start_withp(words):
    """
    Write a function to match two words from a list of words starting with letter 'p'.
    """
    p_words = [word for word in words if word.startswith('p')]
    return p_words[:2]