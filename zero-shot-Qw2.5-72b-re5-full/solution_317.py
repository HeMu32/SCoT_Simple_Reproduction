def modified_encode(alist):
    def encode_helper(lst, count, result):
        if not lst:
            return result
        if lst[0] == lst[1:2]:
            return encode_helper(lst[1:], count + 1, result)
        else:
            result.append((lst[0], count + 1))
            return encode_helper(lst[1:], 0, result)
    return encode_helper(alist, 0, [])