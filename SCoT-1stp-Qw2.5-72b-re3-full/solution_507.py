def remove_words(list1, removewords):
    result = []
    for word in list1:
        if word not in removewords:
            result.append(word)
    return result