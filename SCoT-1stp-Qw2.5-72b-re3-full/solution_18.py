def remove_dirty_chars(string, second_string):
    clean_string = ""
    for char in string:
        if char not in second_string:
            clean_string += char
    return clean_string