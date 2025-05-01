def is_palindrome(arr):
    """
    Write a function to find the largest palindromic number in the given array.
    """
    def is_palindrome_number(n):
        return str(n) == str(n)[::-1]
    
    largest_palindrome = None
    for num in arr:
        if is_palindrome_number(num):
            if largest_palindrome is None or num > largest_palindrome:
                largest_palindrome = num
    return largest_palindrome