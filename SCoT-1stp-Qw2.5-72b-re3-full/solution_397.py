def median_numbers(a, b, c):
    # Create a list of the three numbers
    numbers = [a, b, c]
    # Sort the list in ascending order
    numbers.sort()
    # The median is the middle number in the sorted list
    return numbers[1]