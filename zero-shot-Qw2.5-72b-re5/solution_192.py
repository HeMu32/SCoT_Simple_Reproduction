def check_String(s):
    has_letter = False
    has_number = False
    
    for char in s:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True
        if has_letter and has_number:
            return True
    return False