def rearrange_bigger(n):
    # Convert the integer to a list of its digits
    digits = list(str(n))
    
    # Step 2: Find the pivot
    pivot = -1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i - 1] < digits[i]:
            pivot = i - 1
            break
    
    # Step 3: If no pivot is found, return -1
    if pivot == -1:
        return -1
    
    # Step 4: Find the smallest digit on the right side of the pivot that is larger than the pivot
    for i in range(len(digits) - 1, pivot, -1):
        if digits[i] > digits[pivot]:
            swap_with = i
            break
    
    # Step 5: Swap the pivot with this digit
    digits[pivot], digits[swap_with] = digits[swap_with], digits[pivot]
    
    # Step 6: Sort the digits to the right of the pivot's original position in ascending order
    digits = digits[:pivot + 1] + sorted(digits[pivot + 1:])
    
    # Step 7: Convert the list of digits back to an integer
    result = int(''.join(digits))
    
    # Step 8: Return the new integer
    return result