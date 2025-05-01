def find_Max_Num(digits):
    """
    Write a python function to find the largest number that can be formed with the given digits.
    """
    if not digits:
        return 0
    digits.sort(reverse=True)
    max_number = int(''.join(map(str, digits)))
    return max_number