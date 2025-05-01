def check_Equality(s):
    # Check if the string is empty
    if not s:
        return False
    # Compare the first and last characters
    if s[0] == s[-1]:
        return True
    else:
        return False