def sum_three_smallest_nums(lst):
    positive_nums = [num for num in lst if num > 0]
    if len(positive_nums) < 3:
        return "Not enough positive numbers in the list."
    positive_nums.sort()
    sum_of_three_smallest = sum(positive_nums[:3])
    return sum_of_three_smallest