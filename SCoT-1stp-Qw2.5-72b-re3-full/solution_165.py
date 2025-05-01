def count_char_position(str1):
    count = 0
    str1 = str1.lower()  # Convert the string to lowercase
    for index, char in enumerate(str1):
        # Calculate the position of the character in the alphabet (0-based)
        position = ord(char) - ord('a')
        if position == index:
            count += 1
    return count