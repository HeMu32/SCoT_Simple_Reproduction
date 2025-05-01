def remove_splchar(text):
    result = ""
    for ch in text:
        if ch.isalnum():
            result += ch
    return result