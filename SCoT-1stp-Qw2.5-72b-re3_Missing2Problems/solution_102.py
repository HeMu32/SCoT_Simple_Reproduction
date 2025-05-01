def snake_to_camel(word):
    camelCase = ""
    words = word.split('_')
    for i, w in enumerate(words):
        if i == 0:
            camelCase += w.lower()
        else:
            camelCase += w.capitalize()
    return camelCase