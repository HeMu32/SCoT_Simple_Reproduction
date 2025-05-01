import heapq

def k_smallest_pairs(nums1, nums2, k):
    # Initialize the min-heap
    min_heap = []
    
    # Iterate over each element in nums1 and nums2
    for i in nums1:
        for j in nums2:
            # Calculate the sum of the current pair
            pair_sum = i + j
            
            # If the heap has less than k elements, push the current pair and its sum
            if len(min_heap) < k:
                heapq.heappush(min_heap, (-pair_sum, (i, j)))
            else:
                # If the heap has k elements and the sum of the current pair is less than the largest sum in the heap
                if -min_heap[0][0] > pair_sum:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (-pair_sum, (i, j)))
    
    # Extract the pairs from the heap
    result = [pair for _, pair in min_heap]
    
    # Since the heap is a max-heap (due to negative sums), reverse the result to get the smallest pairs first
    result.reverse()
    
    return result