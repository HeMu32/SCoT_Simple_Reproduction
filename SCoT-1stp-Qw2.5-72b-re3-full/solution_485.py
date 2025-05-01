def largest_palindrome(arr):
    max_palindrome = None
    for num in arr:
        str_num = str(num)
        if str_num == str_num[::-1]:  # Check if the number is a palindrome
            if max_palindrome is None or num > max_palindrome:
                max_palindrome = num
    if max_palindrome is None:
        return "No palindromic number found in the array."
    return max_palindrome