def decode_list(alist):
    decoded_list = []
    for item in alist:
        count, value = item  # Unpack the count and value from the sublist
        for _ in range(count):  # Repeat the value `count` times
            decoded_list.append(value)
    return decoded_list