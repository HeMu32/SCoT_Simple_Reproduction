def text_match_wordz(text):
    found = False
    words = text.split()
    for word in words:
        if 'z' in word:
            found = True
            break
    return found