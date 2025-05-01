import heapq

def heap_assending(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]