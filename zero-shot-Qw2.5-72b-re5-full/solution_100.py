def next_smallest_palindrome(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    num += 1
    while not is_palindrome(num):
        num += 1
    return num