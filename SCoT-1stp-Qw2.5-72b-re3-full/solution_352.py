def unique_Characters(str):
    seen_chars = set()
    for ch in str:
        if ch in seen_chars:
            return False
        seen_chars.add(ch)
    return True