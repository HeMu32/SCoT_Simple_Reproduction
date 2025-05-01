def next_smallest_palindrome(num):
    num += 1  # Start checking from the next number
    while True:
        str_num = str(num)
        if str_num == str_num[::-1]:  # Check if the number is a palindrome
            return num
        num += 1  # Increment the number if it's not a palindrome