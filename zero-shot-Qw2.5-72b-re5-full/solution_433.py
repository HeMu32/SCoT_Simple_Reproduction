def check_greater(arr, number):
    """
    Write a function to check whether the entered number is greater than the elements of the given array.
    """
    return [num < number for num in arr]