def check_String(str):
    has_letter = False
    has_number = False
    
    for ch in str:
        if ch.isalpha():
            has_letter = True
        if ch.isdigit():
            has_number = True
        if has_letter and has_number:
            break
    
    return has_letter and has_number