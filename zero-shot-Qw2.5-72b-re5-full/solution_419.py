def round_and_sum(list1):
    """
    Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
    """
    rounded_list = [round(num) for num in list1]
    total_sum = sum(rounded_list)
    result = total_sum * len(list1)
    print(result)