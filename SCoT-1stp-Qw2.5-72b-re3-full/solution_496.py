import heapq as hq

def heap_queue_smallest(nums, n):
    # Convert the list into a heap in-place
    hq.heapify(nums)
    # Initialize the list to store the n smallest integers
    smallest_n = []
    # Pop the smallest elements from the heap n times
    for i in range(n):
        smallest_n.append(hq.heappop(nums))
    return smallest_n