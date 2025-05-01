def find_Max_Num(digits):
    # Check if the input list is empty
    if not digits:
        return 0  # Return 0 or an appropriate message if the list is empty
    
    # Sort the list of digits in descending order
    digits.sort(reverse=True)
    
    # Convert the sorted list of digits into a single integer
    max_num = int(''.join(map(str, digits)))
    
    # Return the integer as the largest number that can be formed
    return max_num