import heapq

def heap_assending(nums):
    # Convert the list into a heap
    heapq.heapify(nums)
    
    # Initialize an empty list to store the sorted elements
    sorted_nums = []
    
    # Pop elements from the heap and append to the sorted list
    while nums:
        sorted_nums.append(heapq.heappop(nums))
    
    return sorted_nums