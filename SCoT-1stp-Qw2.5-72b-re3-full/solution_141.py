def pancake_sort(nums):
    def flip(sublist, k):
        """Flip the first k elements of the sublist."""
        sublist[:k] = sublist[:k][::-1]

    def find_max_position(sublist, n):
        """Find the position of the maximum element in the first n elements of the sublist."""
        max_pos = 0
        for i in range(1, n):
            if sublist[i] > sublist[max_pos]:
                max_pos = i
        return max_pos

    n = len(nums)
    while n > 1:
        # Find the position of the maximum element in the unsorted portion
        max_pos = find_max_position(nums, n)
        
        # Move the maximum element to the front if it's not already there
        if max_pos != n - 1:
            flip(nums, max_pos + 1)
            flip(nums, n)
        
        # Reduce the size of the unsorted portion
        n -= 1

    return nums